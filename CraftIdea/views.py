from django.shortcuts import render, redirect, get_object_or_404
from CraftIdea.models import CraftIdeaModel, CraftIdeaReview
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    search_term = request.GET.get('search')
    if search_term:
        movies = CraftIdeaModel.objects.filter(title__icontains=search_term)
    else:
        movies = CraftIdeaModel.objects.all()
    template_data = {}
    template_data['title'] = 'Movies'
    template_data['movies'] = movies
    return render(request, 'CraftIdea/index.html',
                  {'template_data': template_data})