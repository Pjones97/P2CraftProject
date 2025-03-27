from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='Crafts.index'),
    path('CraftBot', views.bot, name='Crafts.bot'),
]