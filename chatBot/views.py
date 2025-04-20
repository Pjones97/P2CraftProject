

from django.shortcuts import render
# Create your views here.
# views.py
import requests
from django.http import JsonResponse
from django.conf import settings

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
    return render(request, 'chatBot/index.html')