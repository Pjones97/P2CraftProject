from django.shortcuts import render
# from .models import ....(modelnames)
# Create your views here.

# post = [
#     {
#         'id': 1,
#         'name': 'Custom PC Build',
#         'description': 'Assemble a powerful gaming or workstation PC with hand-picked components.',
#         'video': 'https://www.youtube.com/embed/BLn1NL5bEA8',  # Example embedded link
#         'locations': ['Micro Center', 'Best Buy', 'Newegg (Online)']
#     },
#     {
#         'id': 2,
#         'name': 'Crochet Blanket',
#         'description': 'Create a cozy, handmade blanket using yarn and a crochet hook.',
#         'video': 'https://www.youtube.com/embed/M7YZ8BqKPbY',
#         'locations': ['Joann Fabrics', 'Michaels', 'Hobby Lobby']
#     },
#     {
#         'id': 3,
#         'name': '3D Printed Figurines',
#         'description': 'Design and print custom figurines or prototypes using a 3D printer.',
#         'video': 'https://www.youtube.com/embed/5IuUZMtKlAs',
#         'locations': ['Amazon', 'MatterHackers', 'Micro Center']
#     }
# ]

from django.shortcuts import render, redirect, get_object_or_404
from .models import CraftIdeaModel, CraftIdeaReview
from django.contrib.auth.decorators import login_required


from Media.models import CraftIdeaModel
from accounts.models import Profile




def index(request):
    search_term = request.GET.get('search')
    if search_term:
        crafts = CraftIdeaModel.objects.filter(title__icontains=search_term)
    else:
        crafts = CraftIdeaModel.objects.all()
    template_data = {}
    print("This needs to go here!")
    for craft in crafts:
        print(craft.id)
    template_data['title'] = 'Crafts' # copied this straight from movies ngl
    template_data['crafts'] = crafts
    return render(request, 'Media/index.html',
                  {'template_data': template_data})

def show(request, id):
    craft = CraftIdeaModel.objects.get(id=id)
    reviews = CraftIdeaReview.objects.filter(craft=craft)
    template_data = {}
    template_data['title'] = craft.title
    template_data['craft'] = craft
    template_data['reviews'] = reviews
    template_data['user'] = request.user
    return render(request, 'Media/show.html',
                  {'template_data': template_data})

@login_required
def create_review(request, id):
    if request.method == 'POST' and request.POST['comment'] != '':
        craft = get_object_or_404(CraftIdeaModel, id=id)
        # CraftIdeaModel.objects.get(id=id)
        review = CraftIdeaReview()
        review.comment = request.POST['comment']
        review.craft = craft
        review.user = request.user
        review.save()
        return redirect('Media.show', id=id)
    else:
        return redirect('Media.show', id=id)

@login_required
def edit_review(request, id, review_id):
    review = get_object_or_404(CraftIdeaReview, id=review_id)
    if request.user != review.user:
        return redirect('Media.show', id=id)
    if request.method == 'GET':
        template_data = {}
        template_data['title'] = 'Edit Review'
        template_data['review'] = review
        return render(request, 'Media/edit_review.html',
            {'template_data': template_data})
    elif request.method == 'POST' and request.POST['comment'] != '':
        # review = CraftIdeaReview.objects.get(id=review_id)
        review.comment = request.POST['comment']
        review.save()
        return redirect('Media.show', id=id)
    else:
        return redirect('Media.show', id=id)

@login_required
def delete_review(request, id, review_id):
    review = get_object_or_404(CraftIdeaReview, id=review_id, user=request.user)
    review.delete()
    return redirect('Media.show', id=id)

@login_required
def edit_craft(request, id):
    craft = get_object_or_404(CraftIdeaModel, id=id)
    if request.user != craft.userThatUploaded:
        return redirect('Media.show', id=id)

    if request.method == 'GET':
        template_data = {
            'title': 'Edit Craft',
            'craft': craft,
        }
        return render(request, 'Media/edit_craft.html', {'template_data': template_data})

    elif request.method == 'POST':
        craft.title = request.POST.get('title', craft.title)
        craft.description = request.POST.get('description', craft.description)
        craft.video = request.POST.get('video', craft.video)
        if 'image' in request.FILES:
            craft.image = request.FILES['image']  # Update the image field

        craft.save()
        return redirect('Media.show', id=id)

@login_required
def delete_craft(request, id):
    craft = get_object_or_404(CraftIdeaModel, id=id)
    if request.user == craft.userThatUploaded:
        craft.delete()
    return redirect('Media.index')


# def create_craft(request):
#     craft = CraftIdeaModel() # create a new craft
#     craft.userThatUploaded = request.user
#     print(craft.id)
#     # if request.user != craft.userThatUploaded:
#     #     return redirect('Media.show', id=id)
#
#     if request.method == 'GET':
#         # This is when you are filling out something
#         print("You went inside GET")
#         template_data = {
#             'title': 'Edit Craft',
#             'craft': craft,
#         }
#         return render(request, 'Media/edit_craft.html', {'template_data': template_data})
#
#     elif request.method == 'POST':
#         # This is when you are posting it to the website
#         print("You went inside POST")
#         craft.title = request.POST.get('title', craft.title)
#         print(craft.title)
#         craft.description = request.POST.get('description', craft.description)
#         print(craft.description)
#         craft.video = request.POST.get('video', craft.video)
#         print(craft.video)
#         craft.image = request.POST.get('image', craft.image)
#         print(craft.id)
#         craft.save()
#         return redirect('Media.show', id=craft.id)

@login_required
def create_craft(request):
    if request.method == 'GET':
        print("The Get method started")
        template_data = {
            'title': 'Create New Craft',
            'craft': CraftIdeaModel(),  # Empty craft for the form
        }
        print("The Get method returned")
        return render(request, 'Media/create_craft.html', {'template_data': template_data})

    elif request.method == 'POST':
        # Create new craft instance
        print("The POST method started")
        craft = CraftIdeaModel()
        craft.userThatUploaded = request.user
        craft.title = request.POST.get('title', '')
        craft.description = request.POST.get('description', '')
        craft.video = request.POST.get('video', '')



        print("The handling image")
        # Handle image upload
        if 'image' in request.FILES:
            craft.image = request.FILES['image']

        try:
            print("In try method!")
            craft.save()

            print("The Adding the profile if saving craft was successful!")
            profile = Profile.objects.get(user=request.user)
            profile.user_crafts.add(craft)


            print("about to return redirect")
            return redirect('Media.show', id=craft.id)
        except Exception as e:
            print("Exception was thrown here in the thing hrds")
            # Handle any errors during save
            template_data = {
                'title': 'Create New Craft',
                'craft': craft,
                'error': f'Error creating craft: {str(e)}'
            }
            print("About to return render")
            return render(request, 'Media/create_craft.html', {'template_data': template_data})