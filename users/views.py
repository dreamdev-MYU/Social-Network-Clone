from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import CustomUser, Follow
from .serializers import CustomUserSerializer, FollowSerializer


class UsersAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)


class FollowersAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_id = request.data.get('user_id')
        if user_id:
            try:
                user_to_follow = CustomUser.objects.get(id=user_id)
                follow = Follow.objects.create(following=user_to_follow, follower=request.user)
                serializer = FollowSerializer(follow)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except CustomUser.DoesNotExist:
                return Response({"message": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"message": "User ID is required."}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        follower_id = request.data.get('follower_id')
        if follower_id:
            try:
                follow = Follow.objects.get(id=follower_id, following=request.user)
                follow.is_accepted = True
                follow.save()
                serializer = FollowSerializer(follow)
                return Response(serializer.data)
            except Follow.DoesNotExist:
                return Response({"message": "Follower not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"message": "Follower ID is required."}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        follower_id = request.data.get('follower_id')
        if follower_id:
            try:
                follow = Follow.objects.get(id=follower_id, following=request.user)
                follow.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Follow.DoesNotExist:
                return Response({"message": "Follower not found."}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"message": "Follower ID is required."}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        followers = Follow.objects.filter(following=request.user)
        serializer = FollowSerializer(followers, many=True)
        return Response(serializer.data)
