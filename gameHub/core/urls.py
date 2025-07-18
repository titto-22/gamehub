from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JogoViewSet, CategoriaViewSet, PlataformaViewSet, DesenvolvedoraViewSet
from . import views

router = DefaultRouter()
router.register(r'jogos', JogoViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'plataformas', PlataformaViewSet)
router.register(r'desenvolvedoras', DesenvolvedoraViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('jogos/', views.jogo_list, name='jogo_list'),
    path('jogos/<int:pk>/', views.jogo_detail, name='jogo_detail'),
    path('jogos/novo/', views.jogo_create, name='jogo_create'),
    path('jogos/<int:pk>/editar/', views.jogo_update, name='jogo_update'),
    path('jogos/<int:pk>/deletar/', views.jogo_delete, name='jogo_delete'),
    path('categorias/', views.categoria_list, name='categoria_list'),
    path('categorias/novo/', views.categoria_create, name='categoria_create'),
    path('categorias/<int:pk>/', views.categoria_detail, name='categoria_detail'),
    path('categorias/<int:pk>/editar/', views.categoria_update, name='categoria_update'),
    path('categorias/<int:pk>/deletar/', views.categoria_delete, name='categoria_delete'),
    path('plataformas/', views.plataforma_list, name='plataforma_list'),
    path('plataformas/novo/', views.plataforma_create, name='plataforma_create'),
    path('plataformas/<int:pk>/', views.plataforma_detail, name='plataforma_detail'),
    path('plataformas/<int:pk>/editar/', views.plataforma_update, name='plataforma_update'),
    path('plataformas/<int:pk>/deletar/', views.plataforma_delete, name='plataforma_delete'),
    path('desenvolvedoras/', views.desenvolvedora_list, name='desenvolvedora_list'),
    path('desenvolvedoras/novo/', views.desenvolvedora_create, name='desenvolvedora_create'),
    path('desenvolvedoras/<int:pk>/', views.desenvolvedora_detail, name='desenvolvedora_detail'),
    path('desenvolvedoras/<int:pk>/editar/', views.desenvolvedora_update, name='desenvolvedora_update'),
    path('desenvolvedoras/<int:pk>/deletar/', views.desenvolvedora_delete, name='desenvolvedora_delete'),
    path('avaliacoes/', views.avaliacao_list, name='avaliacao_list'),
    path('avaliacoes/novo/', views.avaliacao_create, name='avaliacao_create'),
    path('avaliacoes/<int:pk>/editar/', views.avaliacao_update, name='avaliacao_update'),
    path('avaliacoes/<int:pk>/deletar/', views.avaliacao_delete, name='avaliacao_delete'),
    path('emprestimos/', views.emprestimo_list, name='emprestimo_list'),
    path('emprestimos/novo/', views.emprestimo_create, name='emprestimo_create'),
    path('emprestimos/<int:pk>/editar/', views.emprestimo_update, name='emprestimo_update'),
    path('emprestimos/<int:pk>/deletar/', views.emprestimo_delete, name='emprestimo_delete'),




]