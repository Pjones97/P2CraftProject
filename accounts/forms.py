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


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.utils import ErrorList
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from .models import Profile


class CustomErrorList(ErrorList):
    def __str__(self):
        if not self:
            return ''
        return mark_safe(''.join([
            f'<div class="alert alert-danger" role="alert">{e}</div>' for e in self]))


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

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2', 'email']:
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
                profile.save()
        return user