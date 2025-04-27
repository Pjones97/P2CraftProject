from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetDoneView
from .views import ForgotPasswordView, ResetConfirm, ResetComplete

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='accounts.signup'),
    path('login/', views.login, name='accounts.login'),
    path('logout/', views.logout, name='accounts.logout'),
   path('password_reset/', ForgotPasswordView.as_view(template_name='accounts/password_reset_form.html'), name='accounts.password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='accounts.password_reset_done'),
    path('reset/<uidb64>/<token>/', ResetConfirm.as_view(template_name='accounts/password_reset_confirm.html'), name='accounts.password_reset_confirm'),
    path('reset/done/', ResetComplete.as_view(template_name='accounts/password_reset_complete.html'), name='accounts.password_reset_complete'),
    path('send-test-email/', views.send_test_email, name='send_test_email'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('<int:id>/view/', views.view_profile, name='view_profile'),
]
