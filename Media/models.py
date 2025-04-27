from django.db import models
from django.contrib.auth.models import User
import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin


# Create your models here.

class CraftIdeaModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    likes = models.ManyToManyField(User, related_name='liked_crafts', blank=True)  # Add this field

    userThatUploaded = models.ForeignKey(User, on_delete=models.CASCADE)  # okay I have no idea if this is right but hey lets give it a shot
    # Profile.user = userThatUploaded
    description = models.TextField()
    image = models.ImageField(upload_to='movie_images/', null=True, blank=True) # horrible name but what can you do
    video = models.URLField(max_length=500, null=True, blank=True)  # horrible name again...

    def like_count(self):
        return self.likes.count()  # Helper method to get the like count
        
    def __str__(self):
        return str(self.id) + ' - ' + self.title #this isn't working
    

    @admin.display(
        #lets show something only admin should see
        boolean=True,
        ordering="title",
        description="The description is here",
    )

    def old_movie(self):
        thing = timezone.now()
        return thing
        


class CraftIdeaReview(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    craft = models.ForeignKey(CraftIdeaModel,
        on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id) + ' - ' + self.craft.title
