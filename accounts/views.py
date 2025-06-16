from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoginSerializer

from django.contrib.auth import authenticate


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data) #requesting data to
        serializer.is_valid(raise_exception=True) #receiving data and deserializing the input of it 
        user = serializer.save() #save new user
        return Response({
            "user": serializer.data,
            "message": "Usuer registered correctly" #confirmation message of the registration of the user
        }, status=status.HTTP_201_CREATED) 


class LoginView(APIView):
    serializer_class = LoginSerializer
        #API to login the user and return jwt tokens
    def post(self, request):
        #post request to login an user, returns access and refresh tokens when succesful login.
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        refresh = RefreshToken.for_user(user)

        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }, status=status.HTTP_200_OK)


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
        #Creating api to handle user logout by  blacklisting the refresh token
    def post(self, request): #post request to logout, blacklist the provided refresh token
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logout Succesful"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
