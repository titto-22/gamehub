from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from core import views
from django.contrib.auth import views as auth_views
from core import views as core_views


def home(request):
    return HttpResponse("Bem-vindo à GameHub API!")


urlpatterns = [
    path('', views.home_page, name='home'),
    path('admin/', admin.site.urls),
    path('', include('core.urls')), 
    path('api/', include('core.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', core_views.register, name='register'),
]
