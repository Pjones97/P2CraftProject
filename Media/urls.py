from django.urls import path
from . import views
urlpatterns = [
    #define path
    path('', views.index, name='Media.index'),
    path('<int:id>/', views.show, name='Media.show'),

path('<int:id>/create/', views.create_media, name='Media.create_media'),
]