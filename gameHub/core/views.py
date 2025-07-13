from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Jogo, Categoria, Plataforma, Desenvolvedora
from .serializers import JogoSerializer, CategoriaSerializer, PlataformaSerializer, DesenvolvedoraSerializer

class JogoViewSet(viewsets.ModelViewSet):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer
    permission_classes = [AllowAny]  # <--- aqui

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [AllowAny]

class PlataformaViewSet(viewsets.ModelViewSet):
    queryset = Plataforma.objects.all()
    serializer_class = PlataformaSerializer
    permission_classes = [AllowAny]

class DesenvolvedoraViewSet(viewsets.ModelViewSet):
    queryset = Desenvolvedora.objects.all()
    serializer_class = DesenvolvedoraSerializer
    permission_classes = [AllowAny]
