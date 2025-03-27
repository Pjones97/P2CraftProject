from django.shortcuts import render

def index(request):
    return render(request, 'Crafts/index.html')

#function renders the Crafts/bot.html template found in Crafts/templates/Crafts
def bot(request):
    return render(request, 'Crafts/bot.html')