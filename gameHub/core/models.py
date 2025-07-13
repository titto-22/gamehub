from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Usuario(AbstractUser):
    data_nascimento = models.DateField(null=True, blank=True)

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

class Plataforma(models.Model):
    nome = models.CharField(max_length=50)

class Desenvolvedora(models.Model):
    nome = models.CharField(max_length=100)

class Jogo(models.Model):
    titulo = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE)
    desenvolvedora = models.ForeignKey(Desenvolvedora, on_delete=models.SET_NULL, null=True)

class Biblioteca(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    jogos = models.ManyToManyField(Jogo, blank=True)

class Avaliacao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    nota = models.IntegerField()
    comentario = models.TextField(blank=True)
    data = models.DateTimeField(auto_now_add=True)

class Emprestimo(models.Model):
    dono = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='emprestimos_dados')
    amigo = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='emprestimos_recebidos')
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField(null=True, blank=True)

class Notificacao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mensagem = models.CharField(max_length=255)
    lida = models.BooleanField(default=False)
    criada_em = models.DateTimeField(auto_now_add=True)

class Favorito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    adicionado_em = models.DateTimeField(auto_now_add=True)
