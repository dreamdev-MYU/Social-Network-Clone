from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='chats', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=200, blank=False, null=False)



    def __str__(self):
        return self.text


    def get_absolute_url(self):
        return reverse('chat', kwargs={
            'chat_id': self.id,
            'username': self.user.username
        })

  
    def get_likes(self):
        return self.liked_chat.count()

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)
    chat = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=200, blank=False, null=False)


    def __str__(self):
        return self.text


class Likes(models.Model):
    chat = models.ForeignKey(Post, related_name='liked_chat', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_liker', on_delete=models.CASCADE)