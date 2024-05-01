from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.conf import settings


class CustomUser(AbstractUser):
    bio = models.TextField(max_length=264)
    location = models.CharField(max_length=128, blank=True, null=True)
    website = models.URLField(max_length=128, blank=True, null=True)
    profilepicture = models.FileField(upload_to='profile_picture', default='nopic.jpeg')

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('useroverview', kwargs={'username': self.username})


class Follow(models.Model):
    following = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='following_set', on_delete=models.CASCADE)
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='follower_set', on_delete=models.CASCADE)
