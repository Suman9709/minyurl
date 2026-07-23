from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from core.serializers import UserRegistrationSerializer,UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ReadOnlyModelViewSet


from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status

from urlshortener.models import User
# Create your views here.

User = get_user_model()

class RegisterUser(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    

class UserViewset(ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    
    
    
class LogoutUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request):

        refresh_token = request.data.get("refresh")

        if not refresh_token:
            return Response(
                {"error": "Refresh token is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(
                {"message": "User logged out successfully."},
                status=status.HTTP_200_OK
            )

        except Exception:
            return Response(
                {"error": "Invalid refresh token."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)