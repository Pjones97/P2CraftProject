from django.shortcuts import render

# Create your views here.

# post = [
#     {
#         'id': 1, 'name': 'Custom PC Build',
#         'description': 'Assemble a powerful gaming or workstation PC with hand-picked components.'
#     },
#     {
#         'id': 2, 'name': 'Crochet Blanket',
#         'description': 'Create a cozy, handmade blanket using yarn and a crochet hook.'
#     },
#     {
#         'id': 3, 'name': '3D Printed Figurines',
#         'description': 'Design and print custom figurines or prototypes using a 3D printer.'
#     },
#     {
#         'id': 4, 'name': 'Handmade Candles',
#         'description': 'Mix wax, fragrance, and color to craft unique scented candles.'
#     },
#     {
#         'id': 5, 'name': 'Arduino Smart Light',
#         'description': 'Build an automated lighting system using an Arduino board and sensors.'
#     },
#     {
#         'id': 6, 'name': 'DIY Leather Wallet',
#         'description': 'Cut, stitch, and assemble a custom leather wallet by hand.'
#     },
#     {
#         'id': 7, 'name': 'Resin Art Coasters',
#         'description': 'Pour and cure epoxy resin mixed with colors and embellishments for unique coasters.'
#     },
#     {
#         'id': 8, 'name': 'Hand-Painted Sneakers',
#         'description': 'Customize sneakers with unique hand-painted designs and colors.'
#     },
#     {
#         'id': 9, 'name': 'DIY Terrarium',
#         'description': 'Assemble a small indoor garden using plants, soil, and decorative elements.'
#     },
#     {
#         'id': 10, 'name': 'Wood-Burning Art',
#         'description': 'Create intricate designs on wood using a pyrography pen.'
#     }
# ]



from django.shortcuts import render, redirect, get_object_or_404
from .models import CraftIdeaModel, CraftIdeaReview
from django.contrib.auth.decorators import login_required


# Create your views here.
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
    template_data['craft'] = crafts
    return render(request, 'Media/index.html',
                  {'template_data': template_data})
# def index(request):
#     template_data = {}
#     template_data['title'] = 'Crafts'
#     template_data['post'] = post
#     return render(request, 'Media/index.html',
#                   {'template_data': template_data})

def show(request, id):
    # alright cool
    craft = CraftIdeaModel.objects.get(id=id)
    print("In show the craft id is", craft.id)
    # reviews = CraftIdeaReview.objects.get(craft=craft)
    template_data = {}
    # template_data['title'] = craft['name']
    template_data['title'] = craft.title
    template_data['craft'] = craft
    # template_data['reviews'] = reviews
    return render(request, 'Media/show.html',
                  {'template_data': template_data})




# How to create new posts!


@login_required
def create_media(request, id):
    if request.method == 'POST' and request.POST['comment'] != '':
        print("We are trying to create a new craft, I bet it won't work though")
        craft = CraftIdeaModel() # I want to make a new craft, so I think this is how I do it
        craft.title = request.POST['title']
        craft.userThatUploaded = request.user.id
        craft.description = request.POST['description']
        craft.image = request.POST['image']
        craft.video = request.POST['video']
        craft.save()

        # review = Review()
        # review.comment = request.POST['comment']
        # review.movie = movie
        # review.user = request.user
        # review.save()
        return redirect('Media.show', id=id)
    else:
        return redirect('Media.show', id=id)

"""
Chat stuff that I have no idea where it goes
# Read the CraftIdeaModel definition from Media/models.py
craft_idea_model_path = os.path.join(extract_path, "Media/models.py")

with open(craft_idea_model_path, "r") as f:
    models_py_content = f.read()

# Display the part of the file that contains CraftIdeaModel
import re

# Extract the CraftIdeaModel class definition
match = re.search(r"class CraftIdeaModel\(.*?\):(.+?)(?=\nclass |\Z)", models_py_content, re.DOTALL)
craft_idea_model_code = match.group(0) if match else "CraftIdeaModel not found."

craft_idea_model_code.strip()

"""

"""
id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    # year = models.IntegerField()
    # price = models.DecimalField(max_digits = 8, decimal_places = 2)
    # director = models.CharField(max_length=200)
    # genre = models.CharField(max_length=200)
    userThatUploaded = models.ForeignKey(User, on_delete=models.CASCADE) # okay I have no idea if this is right but hey lets give it a shot
    description = models.TextField()
    image = models.ImageField(upload_to='movie_images/', null=True, blank=True) # horrible name but what can you do
    video = models.FileField(upload_to='movie_videos/', null=True, blank=True)  # horrible name again...
"""
#
# @login_required
# def edit_review(request, id, review_id):
#     review = get_object_or_404(Review, id=review_id)
#     if request.user != review.user:
#         return redirect('movies.show', id=id)
#     if request.method == 'GET':
#         template_data = {}
#         template_data['title'] = 'Edit Review'
#         template_data['review'] = review
#         return render(request, 'movies/edit_review.html', {'template_data': template_data})
#     elif request.method == 'POST' and request.POST['comment'] != '':
#         review = Review.objects.get(id=review_id)
#         review.comment = request.POST['comment']
#         review.save()
#         return redirect('movies.show', id=id)
#     else:
#         return redirect('movies.show', id=id)
#
# @login_required
# def delete_review(request, id, review_id):
#     review = get_object_or_404(Review, id=review_id, user=request.user)
#     review.delete()
#     return redirect('movies.show', id=id)
#
#
# # Creating reviews for current objects
#
#
# @login_required
# def create_review(request, id):
#     if request.method == 'POST' and request.POST['comment'] != '':
#         movie = Movie.objects.get(id=id)
#         review = Review()
#         review.comment = request.POST['comment']
#         review.movie = movie
#         review.user = request.user
#         review.save()
#         return redirect('movies.show', id=id)
#     else:
#         return redirect('movies.show', id=id)
#
# @login_required
# def edit_review(request, id, review_id):
#     review = get_object_or_404(Review, id=review_id)
#     if request.user != review.user:
#         return redirect('movies.show', id=id)
#     if request.method == 'GET':
#         template_data = {}
#         template_data['title'] = 'Edit Review'
#         template_data['review'] = review
#         return render(request, 'movies/edit_review.html', {'template_data': template_data})
#     elif request.method == 'POST' and request.POST['comment'] != '':
#         review = Review.objects.get(id=review_id)
#         review.comment = request.POST['comment']
#         review.save()
#         return redirect('movies.show', id=id)
#     else:
#         return redirect('movies.show', id=id)
#
# @login_required
# def delete_review(request, id, review_id):
#     review = get_object_or_404(Review, id=review_id, user=request.user)
#     review.delete()
#     return redirect('movies.show', id=id)