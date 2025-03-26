from django.http import request
from django.urls import path
from . import views

import crafts
urlpatterns = [
    #creating a path for the Craft home page
    #links to views file for rendering a template for the set up of this page
    path('', views.index, name='Crafts.index'),
    # path('test/', views.test(request), name='Crafts.test'),



]