from django.urls import path
from . import views
urlpatterns = [
    #define path
    path('', views.index, name='Media.index'),
    path('craft/<int:id>/', views.show, name='Media.show'),
    path('<int:id>/review/create/', views.create_review,
        name='CraftIdeaModel.create_review'),
    path('<int:id>/review/<int:review_id>/edit/',
        views.edit_review, name='CraftIdeaModel.edit_review'),
    path('<int:id>/review/<int:review_id>/delete/',
        views.delete_review, name='CraftIdeaModel.delete_review'),
    path('<int:id>/edit/', views.edit_craft, name='CraftIdeaModel.edit_craft'),
    path('<int:id>/delete/', views.delete_craft, name='CraftIdeaModel.delete_craft'),
]