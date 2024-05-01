# urls.py in posts app
from django.urls import path
from .views import (CommentCreateAPIView, CommentListAPIView,LikeCreateAPIView, 
                    LikeListAPIView,PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView)


app_name = 'posts'

urlpatterns = [
    path('comments/', CommentCreateAPIView.as_view(), name='comment-create'),
    path('posts/<int:post_id>/comments/', CommentListAPIView.as_view(), name='comment-list'),
    path('likes/', LikeCreateAPIView.as_view(), name='like-create'),
    path('posts/<int:post_id>/likes/', LikeListAPIView.as_view(), name='like-list'),
    path('posts/', PostListCreateAPIView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='post-detail'),


]





