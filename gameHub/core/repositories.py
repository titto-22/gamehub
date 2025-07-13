from .models import Jogo


class JogoRepository:
    def get_por_usuario(self, usuario):
        return Jogo.objects.filter(biblioteca__usuario=usuario)