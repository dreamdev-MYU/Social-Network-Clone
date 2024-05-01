# urls.py in users app
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import FollowersAPI, UsersAPI

app_name = 'users'

urlpatterns = [
    path('followers/', FollowersAPI.as_view(), name='followers-api'),
    path('users/', UsersAPI.as_view(), name='users_api'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),



]




