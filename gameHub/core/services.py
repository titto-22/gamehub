class NotificationService:
    def __init__(self, sender):
        self.sender = sender

    def notificar(self, usuario, mensagem):
        self.sender.enviar(usuario.email, mensagem)

class EmailSender:
    def enviar(self, destino, mensagem):
        print(f"Enviando email para {destino}: {mensagem}")
