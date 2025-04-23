from django.contrib import admin

# Register your models here.




from django.contrib import admin

# from .models import Movie

# admin.site.register(Movie)
# These lines of code allow you to see the Movie's that we have available


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)
    list_display = ('username', 'email', 'get_picture')

    def get_picture(self, instance):
        return instance.profile.picture.url if instance.profile.picture else None

    get_picture.short_description = 'Profile Picture'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)