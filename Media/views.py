from django.shortcuts import render

# Create your views here.

post = [
    {
        'id': 1, 'name': 'Custom PC Build',
        'description': 'Assemble a powerful gaming or workstation PC with hand-picked components.'
    },
    {
        'id': 2, 'name': 'Crochet Blanket',
        'description': 'Create a cozy, handmade blanket using yarn and a crochet hook.'
    },
    {
        'id': 3, 'name': '3D Printed Figurines',
        'description': 'Design and print custom figurines or prototypes using a 3D printer.'
    },
    {
        'id': 4, 'name': 'Handmade Candles',
        'description': 'Mix wax, fragrance, and color to craft unique scented candles.'
    },
    {
        'id': 5, 'name': 'Arduino Smart Light',
        'description': 'Build an automated lighting system using an Arduino board and sensors.'
    },
    {
        'id': 6, 'name': 'DIY Leather Wallet',
        'description': 'Cut, stitch, and assemble a custom leather wallet by hand.'
    },
    {
        'id': 7, 'name': 'Resin Art Coasters',
        'description': 'Pour and cure epoxy resin mixed with colors and embellishments for unique coasters.'
    },
    {
        'id': 8, 'name': 'Hand-Painted Sneakers',
        'description': 'Customize sneakers with unique hand-painted designs and colors.'
    },
    {
        'id': 9, 'name': 'DIY Terrarium',
        'description': 'Assemble a small indoor garden using plants, soil, and decorative elements.'
    },
    {
        'id': 10, 'name': 'Wood-Burning Art',
        'description': 'Create intricate designs on wood using a pyrography pen.'
    }
]



from django.shortcuts import render, redirect, get_object_or_404
from .models import CraftIdeaModel, CraftIdeaReview
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    search_term = request.GET.get('search')
    if search_term:
        movies = CraftIdeaModel.objects.filter(title__icontains=search_term)
    else:
        movies = CraftIdeaModel.objects.all()
    template_data = {}
    template_data['title'] = 'Movies' # copied this straight from movies ngl
    template_data['craft'] = movies
    return render(request, 'Media/index.html',
                  {'template_data': template_data})
# def index(request):
#     template_data = {}
#     template_data['title'] = 'Crafts'
#     template_data['post'] = post
#     return render(request, 'Media/index.html',
#                   {'template_data': template_data})

def show(request, id):
    craft = post[id - 1]
    template_data = {}
    template_data['title'] = craft['name']
    template_data['craft'] = craft
    return render(request, 'Media/show.html',
                  {'template_data': template_data})