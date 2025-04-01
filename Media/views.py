from django.shortcuts import render

# Create your views here.

post = [
    {
        'id': 1,
        'name': 'Custom PC Build',
        'description': 'Assemble a powerful gaming or workstation PC with hand-picked components.',
        'video': 'https://www.youtube.com/embed/BLn1NL5bEA8',  # Example embedded link
        'locations': ['Micro Center', 'Best Buy', 'Newegg (Online)']
    },
    {
        'id': 2,
        'name': 'Crochet Blanket',
        'description': 'Create a cozy, handmade blanket using yarn and a crochet hook.',
        'video': 'https://www.youtube.com/embed/M7YZ8BqKPbY',
        'locations': ['Joann Fabrics', 'Michaels', 'Hobby Lobby']
    },
    {
        'id': 3,
        'name': '3D Printed Figurines',
        'description': 'Design and print custom figurines or prototypes using a 3D printer.',
        'video': 'https://www.youtube.com/embed/5IuUZMtKlAs',
        'locations': ['Amazon', 'MatterHackers', 'Micro Center']
    }
]


def index(request):
    template_data = {}
    template_data['title'] = 'Crafts'
    template_data['post'] = post
    return render(request, 'Media/index.html',
                  {'template_data': template_data})

def show(request, id):
    craft = post[id - 1]
    template_data = {}
    template_data['title'] = craft['name']
    template_data['craft'] = craft
    return render(request, 'Media/show.html',
                  {'template_data': template_data})