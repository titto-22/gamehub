from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JogoViewSet, CategoriaViewSet, PlataformaViewSet, DesenvolvedoraViewSet

router = DefaultRouter()
router.register(r'jogos', JogoViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'plataformas', PlataformaViewSet)
router.register(r'desenvolvedoras', DesenvolvedoraViewSet)

urlpatterns = [
    path('', include(router.urls)),
]