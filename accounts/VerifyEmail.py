from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

class VerifyEmailView(APIView):
    def get(self, request):
        token = request.GET.get('token')
        # TODO: Validar token y obtener usuario
        user = ...  # lógica para extraer el usuario del token
        if user:
            user.is_active = True
            user.save()
            return Response({"message": "Email verified successfully"})
        return Response({"error": "Invalid token"}, status=400)
