

from django.shortcuts import render
# Create your views here.
# views.py
import requests
from django.http import JsonResponse
from django.conf import settings
from .models import Message

def fetch_youtube_videos(request):
    print("YouTube API view called!") 
    craft_idea = request.GET.get("q")  # like "DIY clay pot"
    if not craft_idea:
        return JsonResponse({"error": "No query provided"}, status=400)

    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": craft_idea,
        "type": "video",
        "key": settings.YOUTUBE_API_KEY,
        "maxResults": 10,
    }
    response = requests.get(url, params=params)
    data = response.json()

    video_list = [
        {
            "title": item["snippet"]["title"],
            "videoId": item["id"]["videoId"],
            "thumbnail": item["snippet"]["thumbnails"]["medium"]["url"],
        }
        for item in data.get("items", [])
    ]

    return JsonResponse({"videos": video_list})


def index(request):
    messages = Message.objects.all().order_by('timestamp')
    return render(request, 'chatBot/index.html')

def chat_view(request):
    if request.method == "POST":
        user_message = request.POST.get('message')
        bot_message = get_ai_response(user_message)

        Message.objects.create(user_message=user_message, bot_message=bot_message)

        messages = Message.objects.all().order_by('timestamp')  # You have timestamp field

        # 👇 This is critical
        if request.headers.get('Hx-Request'):
            # HTMX request: return only chat messages partial
            return render(request, 'chatbox.html', {'messages': messages})
        else:
            # Regular POST (fallback): return full page
            return render(request, 'chatBot/index.html', {'messages': messages})

    # GET request: load full page
    messages = Message.objects.all().order_by('timestamp')
    return render(request, 'chatBot/index.html', {'messages': messages})    

def get_ai_response(user_input: str) -> str:
    # Set up the API endpoint and headers
    endpoint = "https://api.openai.com/v1/chat/completions"
    headers = {
        #JDH is just the name of my API key, everything else is supposed to be secret
        "Authorization": f"Bearer {settings.OPENAI_API_KEY}",  
        "Content-Type": "application/json",
    }

    # Data payload
    messages = get_existing_messages()
    messages.append({"role": "user", "content": f"{user_input}"})
    data = {
        "model": "gpt-3.5-turbo",
        "messages": messages,
        "temperature": 0.7
    }
    response = requests.post(endpoint, headers=headers, json=data)
    response_data = response.json()



    if 'choices' in response_data:
        ai_message = response_data['choices'][0]['message']['content']
    else:
        print("OpenAI API error:", response_data)
        ai_message = "Sorry, something went wrong with the AI."

    return ai_message


def get_existing_messages() -> list:
    """
    Get all messages from the database and format them for the API.
    """
    formatted_messages = []

    for message in Message.objects.values('user_message', 'bot_message'):
        formatted_messages.append({"role": "user", "content": message['user_message']})
        formatted_messages.append({"role": "assistant", "content": message['bot_message']})

    return formatted_messages