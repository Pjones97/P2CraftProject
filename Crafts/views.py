from django.shortcuts import render

def index(request):
    template_data = {}
    template_data['title'] = 'Projexis'
    return render(request, 'Crafts/index.html', {
        'template_data': template_data})
#function renders the Crafts/bot.html template found in Crafts/templates/Crafts
