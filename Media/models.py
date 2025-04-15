from django.db import models

# Create your models here.




from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models
# class Movie(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#     price = models.IntegerField()
#     description = models.TextField()
#     image = models.ImageField(upload_to='movie_images/')
#     def __str__(self):
#         return str(self.id) + ' - ' + self.name


import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin



class CraftIdeaModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    # year = models.IntegerField()
    # price = models.DecimalField(max_digits = 8, decimal_places = 2)
    # director = models.CharField(max_length=200)
    # genre = models.CharField(max_length=200)
    userThatUploaded = models.ForeignKey(User, on_delete=models.CASCADE) # okay I have no idea if this is right but hey lets give it a shot
    description = models.TextField()
    image = models.ImageField(upload_to='movie_images/', null=True, blank=True) # horrible name but what can you do
    video = models.FileField(upload_to='movie_videos/', null=True, blank=True)  # horrible name again...

    # rating = models.DecimalField(max_digits=3, default=1, decimal_places=2)
    def __str__(self):
        return str(self.id) + ' - ' + self.title #this isn't working
    # poster = models.ImageField(upload_to='posters/') # Cannot use ImageField because Pillow is not installed
    # def __str__(self):
    #     return self.title
    # def get_price(self):
    #     return self.price
    # def old_movie(self):
    #     return self.year < 2005

    @admin.display(
        #lets show something only admin should see
        boolean=True,
        ordering="title",
        description="The description is here",
    )

    def old_movie(self):
        thing = timezone.now()
        return thing
        # now = timezone.now()
        # return now > datetime.datetime(year=2025, month = 1, day = 1)


class CraftIdeaReview(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    craft = models.ForeignKey(CraftIdeaModel,
        on_delete=models.CASCADE)
    user = models.ForeignKey(User,
        on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id) + ' - ' + self.craft.title