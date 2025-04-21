#
# from . import views
#
#
# from django.urls import path
# # from .views import user_login, signup
# # from django.contrib.auth.views import LogoutView
#
# #urls is what the urls that we have available,
# # as we add new pages, we need to urls, which is the first value in the path function
# # the second is basically which function it is going to use from views.py
# # the last is basically a field that allow us to see where we are in the website
# # name isn't the only thing we can add
#
#
# urlpatterns = [
#     path('', views.index, name='index'),
#     # this should have all of our movie lists together, then have a login button in the top right and a register button.
#     # we can have a login button, and there it has a "register here" in there like most websites, which wouldn't be hard to change the path underneath as you'll see ***
#     # 'login/register' actually that doesn't make sense
#     path('signup/', views.signup, name='accounts.signup'),
#     path('login/', views.login, name='accounts.login'),
#     path('logout/', views.logout, name='accounts.logout'),
#
# ]



from . import views


from django.urls import path, include
# from .views import user_login, signup
# from django.contrib.auth.views import LogoutView

#urls is what the urls that we have available,
# as we add new pages, we need to urls, which is the first value in the path function
# the second is basically which function it is going to use from views.py
# the last is basically a field that allow us to see where we are in the website
# name isn't the only thing we can add
from django.contrib.auth.views import (
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from .views import ForgotPasswordView, ResetConfirm
from .views import ResetComplete


urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='accounts.signup'),
    path('login/', views.login, name='accounts.login'),
    path('logout/', views.logout, name='accounts.logout'),


    path('password_reset/', ForgotPasswordView.as_view(), name='accounts.password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
         name='accounts.password_reset_done'),
    path('reset/<uidb64>/<token>/',
         ResetConfirm.as_view(),
         name='accounts.password_reset_confirm'),

    path('reset/done/',  ResetComplete.as_view(), name='accounts.password_reset_complete'),
    path('send-test-email/', views.send_test_email, name='send_test_email'),
    path('update_profile/', views.update_profile, name='update_profile'),


]


