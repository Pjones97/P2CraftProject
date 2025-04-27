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
from django.contrib.auth.decorators import login_required



import googlemaps
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import ProfileForm
import googlemaps
import json
from django.conf import settings


def update_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            address = form.cleaned_data['location']

            # Handle Google Maps geocoding if needed
            if address and hasattr(settings, 'GOOGLE_MAPS_API_KEY'):
                try:
                    gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
                    geocode_result = gmaps.geocode(address)
                    if geocode_result:
                        profile.latitude = geocode_result[0]['geometry']['location']['lat']
                        profile.longitude = geocode_result[0]['geometry']['location']['lng']
                except Exception as e:
                    # Handle API errors gracefully
                    print(f"Geocoding error: {e}")

            # Save the profile first
            profile.save()

            # Save many-to-many fields
            form.save_m2m()

            return redirect('accounts.index')
    else:
        form = ProfileForm(instance=request.user.profile)

    return render(request, 'accounts/update_profile.html', {'form': form})

# def update_profile(request):
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             address = form.cleaned_data['location']
#             gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
#             print("This line works!")
#             geocode_result = gmaps.geocode(address) #This gives an error... saying
#             print("I hope this line works")
#             """
#             ApiError at /accounts/update_profile/
#             REQUEST_DENIED (This API project is not authorized to use this API.)
#             """
#             if geocode_result:
#                 profile.latitude = geocode_result[0]['geometry']['location']['lat']
#                 print("latitdue", profile.latitude)
#                 profile.longitude = geocode_result[0]['geometry']['location']['lng']
#                 print("longitude", profile.longitude)
#             profile.save()
#             return redirect('index') #this goes back to index
#     else:
#         form = ProfileForm(instance=request.user.profile)
#     return render(request, 'accounts/update_profile.html', {'form': form})

import googlemaps
from django.conf import settings

def get_location_details(address):
    gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
    geocode_result = gmaps.geocode(address)
    return geocode_result

#
# def update_profile(request):
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
#         if form.is_valid():
#             profile = form.save(commit=False)
#             address = form.cleaned_data['location']
#             gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
#             geocode_result = gmaps.geocode(address)
#             if geocode_result:
#                 profile.latitude = geocode_result[0]['geometry']['location']['lat']
#                 profile.longitude = geocode_result[0]['geometry']['location']['lng']
#             profile.save()
#             return redirect('profile')
#     else:
#         form = ProfileForm(instance=request.user.profile)
#     return render(request, 'accounts/update_profile.html', {'form': form})


@login_required
def index(request):
    # tbh I feel like there is more stuff that I should add

    # Get the user's liked crafts and user crafts
    liked_crafts = request.user.profile.liked_crafts.all()
    user_crafts = request.user.profile.user_crafts.all()
    for thing in liked_crafts:
        print("Liked Craft:", thing)
    for thing2 in user_crafts:
        print("Your Craft", thing2)
    context = {
        'liked_crafts': liked_crafts,
        'user_crafts': user_crafts,
    }
    return render(request, 'accounts/index.html', context)

# @login_required  #anyone can see other people's crafts
# views 1.py
from django.shortcuts import render, get_object_or_404
from accounts.models import Profile

def view_profile(request, id):
    thisProfile = get_object_or_404(Profile, pk=id)
    thisUser_crafts = thisProfile.user_crafts.all()
    context = {
        'thisProfile': thisProfile,
        'user_crafts': thisUser_crafts,
    }
    return render(request, 'accounts/view_profile.html', context)


from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from .forms import CustomUserCreationForm, CustomErrorList
from django.shortcuts import redirect

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

# def signup(request):
#     template_data = {}
#     template_data['title'] = 'Sign Up'
#     if request.method == 'GET':
#         template_data['form'] = CustomUserCreationForm()
#         return render(request, 'accounts/signup.html',
#             {'template_data': template_data})
#     elif request.method == 'POST':
#         form = CustomUserCreationForm(request.POST, error_class=CustomErrorList)
#         if form.is_valid():
#             form.save()
#             return redirect('accounts.login')
#         else:
#             template_data['form'] = form
#             return render(request, 'accounts/signup.html',
#                 {'template_data': template_data})


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


def signup(request):
    template_data = {}
    template_data['title'] = 'Sign Up'
    if request.method == 'GET':
        template_data['form'] = CustomUserCreationForm()
        return render(request, 'accounts/signup.html',
            {'template_data': template_data})
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES, error_class=CustomErrorList)
        if form.is_valid():
            form.save()
            return redirect('accounts.login')
        else:
            template_data['form'] = form
            return render(request, 'accounts/signup.html',
                {'template_data': template_data})