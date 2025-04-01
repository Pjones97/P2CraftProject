from django.contrib import admin

# Register your models here.


from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import CraftIdeaModel, CraftIdeaReview
admin.site.register(CraftIdeaModel)
admin.site.register(CraftIdeaReview)