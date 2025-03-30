#
# from . import views
#
#

from . import views


from django.urls import path, include
# from .views import user_login, signup
# from django.contrib.auth.views import LogoutView

#urls is what the urls that we have available,
# as we add new pages, we need to urls, which is the first value in the path function
# the second is basically which function it is going to use from views.py
# the last is basically a field that allow us to see where we are in the website
# name isn't the only thing we can add
]

urlpatterns = [
    path('', views.index, name='movies.index'),
    path('<int:id>/', views.show, name='movies.show'),
    path('<int:id>/review/create/', views.create_review, name='movies.create_review'),
    path('<int:id>/review/<int:review_id>/edit/', views.edit_review, name='movies.edit_review'),
    path('<int:id>/review/<int:review_id>/delete/', views.delete_review, name='movies.delete_review'),

]


