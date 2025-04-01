from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.urls import reverse_lazy

from django.shortcuts import render, redirect

# from accounts.models import Movie


# Create your views here.
# Our views page actually shows what the consumer is viewing
# a pretty convienient name

def index(request):
    return HttpResponse("Hello, world. You're at the index.")


from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from .forms import CustomUserCreationForm, CustomErrorList
from django.shortcuts import redirect


from django.contrib.auth.decorators import login_required
@login_required
def logout(request):
    auth_logout(request)
    return redirect('Crafts.index') # Go to Crafts/urls and this is the name of the index!!!!
def login(request):
    template_data = {}
    template_data['title'] = 'Login'
    if request.method == 'GET':
        return render(request, 'accounts/login.html',
            {'template_data': template_data})
    elif request.method == 'POST':
        user = authenticate(
            request,
            username = request.POST['username'],
            password = request.POST['password']
        )
        if user is None:
            template_data['error'] = 'The username or password is incorrect.'
            return render(request, 'accounts/login.html',
                {'template_data': template_data})
        else:
            auth_login(request, user)
            return redirect('Crafts.index')

def signup(request):
    template_data = {}
    template_data['title'] = 'Sign Up'
    if request.method == 'GET':
        template_data['form'] = CustomUserCreationForm()
        return render(request, 'accounts/signup.html',
            {'template_data': template_data})
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST, error_class=CustomErrorList)
        if form.is_valid():
            form.save()
            return redirect('accounts.login')
        else:
            template_data['form'] = form
            return render(request, 'accounts/signup.html',
                {'template_data': template_data})


from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.forms import PasswordResetForm
from django.urls import reverse_lazy


class ForgotPasswordView(PasswordResetView):
    template_name = 'accounts/forgot_password.html'  # Use your custom HTML file
    email_template_name = 'accounts/password_reset_email.html'  # Email template
    subject_template_name = 'accounts/password_reset_subject.txt'  # Email subject template
    success_url = reverse_lazy('accounts.password_reset_done')  # Redirect after form submission to "Email sent, go back to home page"
    # TODO see if you should have accounts.password_reset_done or password_reset_done
    # its not redirecting me!

from django.contrib.auth.views import PasswordResetCompleteView
from django.urls import reverse_lazy

class ResetConfirm(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts.password_reset_complete')

class ResetComplete(PasswordResetCompleteView):
    # Specify the template to display the success message
    template_name = 'accounts/password_reset_complete.html'
    # success_url = reverse_lazy('accounts.login')



from django.core.mail import send_mail
from django.http import HttpResponse


def send_test_email(request):
    try:
        send_mail(
            subject='Test Email from Django',
            message='This is a test email.',
            from_email=None,  # Defaults to DEFAULT_FROM_EMAIL in settings.py
            recipient_list=['falsebooks3@gmail.com'],  # Replace with your recipient's email
            fail_silently=False,
        )
        return HttpResponse("Test email sent successfully.")
    except Exception as e:
        return HttpResponse(f"Failed to send email: {e}")
