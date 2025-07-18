from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


def home(request):
    return HttpResponse("Bem-vindo à GameHub API!")


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # API endpoints
    path('api/', include('core.urls')),  # DRF rotas (ViewSets etc.)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Views HTML
    path('', include('core.urls')),  # <-- Isso permite acessar /jogos/ e etc.
    path('home/', home),
]
