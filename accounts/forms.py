# # from django.contrib.auth.forms import UserCreationForm
# # from django.contrib.auth.forms import UserCreationForm
# # from django.forms.utils import ErrorList
# # from django.utils.safestring import mark_safe
# # class CustomErrorList(ErrorList):
# #     def __str__(self):
# #         if not self:
# #             return ''
# #         return mark_safe(''.join([
# #             f'<div class="alert alert-danger" role="alert">{e}</div>' for e in self]))
# #
# # class CustomUserCreationForm(UserCreationForm):
# #     def __init__(self, *args, **kwargs):
# #         super(CustomUserCreationForm, self).__init__(*args, **kwargs)
# #         for fieldname in ['username', 'password1',
# #         'password2']:
# #             self.fields[fieldname].help_text = None
# #             self.fields[fieldname].widget.attrs.update(
# #                 {'class': 'form-control'}
# #             )
# # Commented it out jic we need it
#
# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.forms.utils import ErrorList
# from django.utils.safestring import mark_safe
# from django.contrib.auth.models import User
#
#
# class CustomErrorList(ErrorList):
#     def __str__(self):
#         if not self:
#             return ''
#         return mark_safe(''.join([
#             f'<div class="alert alert-danger" role="alert">{e}</div>' for e in self]))
#
#
# class CustomUserCreationForm(UserCreationForm):
#     email = forms.EmailField(
#         required=True,
#         widget=forms.EmailInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Enter your email address',
#         }),
#         help_text="Please enter a valid email address.",
#     )
#
#     picture = forms.ImageField(required=False) # I hope this is on the right track
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
#
#     def __init__(self, *args, **kwargs):
#         super(CustomUserCreationForm, self).__init__(*args, **kwargs)
#         for fieldname in ['username', 'password1', 'password2', 'email']:
#             self.fields[fieldname].help_text = None
#             self.fields[fieldname].widget.attrs.update(
#                 {'class': 'form-control'}
#             )
#
#     def save(self, commit=True):
#         user = super(CustomUserCreationForm, self).save(commit=False)
#         user.email = self.cleaned_data['email']
#         user.picture = self.cleaned_data['picture']
#         if commit:
#             user.save()
#         return user

#
# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.forms.utils import ErrorList
# from django.utils.safestring import mark_safe
# from django.contrib.auth.models import User
# from .models import Profile
#
#
# class CustomErrorList(ErrorList):
#     def __str__(self):
#         if not self:
#             return ''
#         return mark_safe(''.join([
#             f'<div class="alert alert-danger" role="alert">{e}</div>' for e in self]))
#
#
# class CustomUserCreationForm(UserCreationForm):
#     email = forms.EmailField(
#         required=True,
#         widget=forms.EmailInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Enter your email address',
#         }),
#         help_text="Please enter a valid email address.",
#     )
#
#     picture = forms.ImageField(required=False, widget=forms.FileInput(attrs={
#         'class': 'form-control',
#     }))
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
#
#     def __init__(self, *args, **kwargs):
#         super(CustomUserCreationForm, self).__init__(*args, **kwargs)
#         for fieldname in ['username', 'password1', 'password2', 'email']:
#             self.fields[fieldname].help_text = None
#             self.fields[fieldname].widget.attrs.update(
#                 {'class': 'form-control'}
#             )
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.email = self.cleaned_data['email']
#         if commit:
#             user.save()
#             profile = Profile.objects.get(user=user)
#             if self.cleaned_data['picture']:
#                 profile.picture = self.cleaned_data['picture']
#                 profile.save()
#         return user


#
# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.forms.utils import ErrorList
# from django.utils.safestring import mark_safe
# from django.contrib.auth.models import User
# from .models import Profile
#
# class CustomErrorList(ErrorList):
#     def __str__(self):
#         if not self:
#             return ''
#         return mark_safe(''.join([
#             f'<div class="alert alert-danger" role="alert">{e}</div>' for e in self
#         ]))
#
# class CustomUserCreationForm(UserCreationForm):
#     email = forms.EmailField(
#         required=True,
#         widget=forms.EmailInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Enter your email address',
#         }),
#         help_text="Please enter a valid email address.",
#     )
#     picture = forms.ImageField(required=False, widget=forms.FileInput(attrs={
#         'class': 'form-control',
#     }))
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
#
#     def __init__(self, *args, **kwargs):
#         super(CustomUserCreationForm, self).__init__(*args, **kwargs)
#         for fieldname in ['username', 'password1', 'password2', 'email']:
#             self.fields[fieldname].help_text = None
#             self.fields[fieldname].widget.attrs.update(
#                 {'class': 'form-control'}
#             )
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.email = self.cleaned_data['email']
#         if commit:
#             user.save()
#         profile = Profile.objects.get(user=user)
#         if self.cleaned_data['picture']:
#             profile.picture = self.cleaned_data['picture']
#         profile.save()
#         return user
#
# class ProfileForm(forms.ModelForm):
#     location = forms.CharField(
#         required=False,
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Enter your location',
#         })
#     )
#
#     class Meta:
#         model = Profile
#         fields = ['picture', 'location', 'liked_crafts', 'user_crafts']
#
#     def __init__(self, *args, **kwargs):
#         super(ProfileForm, self).__init__(*args, **kwargs)
#         for fieldname in ['picture', 'location', 'liked_crafts', 'user_crafts']:
#             self.fields[fieldname].widget.attrs.update(
#                 {'class': 'form-control'}
#             )





# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.forms.utils import ErrorList
# from django.utils.safestring import mark_safe
# from django.contrib.auth.models import User
# from .models import Profile
#
# class CustomErrorList(ErrorList):
#     def __str__(self):
#         if not self:
#             return ''
#         return mark_safe(''.join([
#             f'<div class="alert alert-danger" role="alert">{e}</div>' for e in self
#         ]))
#
# class CustomUserCreationForm(UserCreationForm):
#     email = forms.EmailField(
#         required=True,
#         widget=forms.EmailInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Enter your email address',
#         }),
#         help_text="Please enter a valid email address.",
#     )
#     picture = forms.ImageField(required=False, widget=forms.FileInput(attrs={
#         'class': 'form-control',
#     }))
#     location = forms.CharField(
#         required=False,
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Enter your location',
#         })
#     )
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2', 'picture', 'location']
#
#     def __init__(self, *args, **kwargs):
#         super(CustomUserCreationForm, self).__init__(*args, **kwargs)
#         for fieldname in ['username', 'password1', 'password2', 'email', 'picture', 'location']:
#             self.fields[fieldname].help_text = None
#             self.fields[fieldname].widget.attrs.update(
#                 {'class': 'form-control'}
#             )
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.email = self.cleaned_data['email']
#         if commit:
#             user.save()
#         profile = Profile.objects.get(user=user)
#         if self.cleaned_data['picture']:
#             profile.picture = self.cleaned_data['picture']
#         if self.cleaned_data['location']:
#             profile.location = self.cleaned_data['location']
#         profile.save()
#         return user




from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.utils import ErrorList
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from .models import Profile


from django import forms
from .models import Profile


class CustomErrorList(ErrorList):
    def __str__(self):
        if not self:
            return ''
        return mark_safe(''.join([
            f'<div class="alert alert-danger" role="alert">{e}</div>' for e in self
        ]))

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email address',
        }),
        help_text="Please enter a valid email address.",
    )
    picture = forms.ImageField(required=False, widget=forms.FileInput(attrs={
        'class': 'form-control',
    }))
    location = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your location',
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'picture', 'location']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2', 'email', 'picture', 'location']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update(
                {'class': 'form-control'}
            )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        profile = Profile.objects.get(user=user)
        if self.cleaned_data['picture']:
            profile.picture = self.cleaned_data['picture']
        if self.cleaned_data['location']:
            profile.location = self.cleaned_data['location']
        profile.save()
        return user


class ProfileForm(forms.ModelForm):
    location = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your location',
        })
    )

    class Meta:
        model = Profile
        fields = ['picture', 'location', 'liked_crafts', 'user_crafts']
        # Meta defines the things that you update in your profile, so you update your pic, location, and liked_crafts and user_crafts

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for fieldname in ['picture', 'location', 'liked_crafts', 'user_crafts']: # took out 'liked_crafts' and 'user_crafts'  on lines 346 and 341!!
            self.fields[fieldname].widget.attrs.update(
                {'class': 'form-control'}
            )

"""
Thank you for your kind words! I'm glad to help. Let's break down the CustomUserCreationForm and ProfileForm in your forms.py to clarify their roles and how they work together.

CustomUserCreationForm
Purpose: This form is used during the signup process to create a new user account. It includes fields for the user's basic information and profile details.

Fields:

username
email
password1
password2
picture
location
Meta Class: The Meta class inside CustomUserCreationForm specifies the model that the form is based on (User) and the fields to include in the form. This ensures that the form fields correspond to the attributes of the User model.

ProfileForm
Purpose: This form is used to update the user's profile after the account has been created. It includes fields for profile-specific information.

Fields:

picture
location
liked_crafts
user_crafts
Meta Class: The Meta class inside ProfileForm specifies the model that the form is based on (Profile) and the fields to include in the form. This ensures that the form fields correspond to the attributes of the Profile model.

Explanation of Internal Meta Class
The Meta class in Django forms is used to define metadata for the form. It specifies:

Model: The model that the form is associated with.
Fields: The fields from the model that should be included in the form.
Why Two Locations?
CustomUserCreationForm: This form is used during signup, where the user provides initial information, including their location.
ProfileForm: This form is used for updating the profile after signup. It allows users to update their location and other profile details.
Accessing ProfileForm
Users can access the ProfileForm through a view that handles profile updates. You can create a link to this view in your HTML templates. Here's an example:

Example View for ProfileForm
import googlemaps
from django.conf import settings
from django.shortcuts import render, redirect
from .forms import ProfileForm

def update_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            address = form.cleaned_data['location']
            gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
            geocode_result = gmaps.geocode(address)
            if geocode_result:
                profile.latitude = geocode_result[0]['geometry']['location']['lat']
                profile.longitude = geocode_result[0]['geometry']['location']['lng']
            profile.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'accounts/update_profile.html', {'form': form})
Example Template Link
You can add a link to the profile update page in your HTML templates:

<a href="{% url 'update_profile' %}">Update Profile</a>
Using CharField for Location
The CharField for location stores the address as a string. The Google Maps API can use this string to perform geocoding, converting the address into latitude and longitude coordinates.

Summary
CustomUserCreationForm: Used during signup to create a new user account.
ProfileForm: Used to update the user's profile after signup.
Meta Class: Specifies the model and fields for the form.
Accessing ProfileForm: Create a view and link to handle profile updates.
By understanding these forms and their roles, you can effectively manage user signup and profile updates in your Django project.

Does this help clarify things? If you have any more questions or need further assistance, feel free to ask!
"""