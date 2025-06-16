from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Endpoints JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),      # Para login (obtener access y refresh)
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),     # Refrescar access token
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),        # Verificar token válido

    # Endpoints propios de tu app 'accounts'
    path('api/', include('accounts.urls')),  # Ej. /api/register/, /api/login/, /api/logout/
]
