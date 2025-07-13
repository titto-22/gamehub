from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Usuario(AbstractUser):
    data_nascimento = models.DateField(null=True, blank=True)

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome

class Plataforma(models.Model):
    nome = models.CharField(max_length=50)
    def __str__(self):
        return self.nome

class Desenvolvedora(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class Jogo(models.Model):
    titulo = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE)
    desenvolvedora = models.ForeignKey(Desenvolvedora, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.titulo

class Biblioteca(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    jogos = models.ManyToManyField(Jogo, blank=True)

class Avaliacao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    nota = models.IntegerField()
    comentario = models.TextField(blank=True)
    data = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.usuario.username} avaliou {self.jogo.titulo} com nota {self.nota}"

class Emprestimo(models.Model):
    dono = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='emprestimos_dados')
    amigo = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='emprestimos_recebidos')
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Empréstimo de {self.jogo.titulo} por {self.dono.username} para {self.amigo.username}"

class Notificacao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mensagem = models.CharField(max_length=255)
    lida = models.BooleanField(default=False)
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mensagem


class Favorito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)
    adicionado_em = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.jogo.titulo
