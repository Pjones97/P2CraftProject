from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='chatBot.index'),
    path("api/youtube/", views.fetch_youtube_videos, name="youtube_videos"),
    path('openai/', views.chat_view, name='chat_view'), 
]