# core/forms.py
from django import forms
from .models import Jogo, Categoria, Plataforma, Desenvolvedora,Biblioteca, Avaliacao, Emprestimo, Notificacao

class JogoForm(forms.ModelForm):
    class Meta:
        model = Jogo
        fields = ['titulo', 'descricao', 'plataforma', 'desenvolvedora', 'categoria']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']

class PlataformaForm(forms.ModelForm):
    class Meta:
        model = Plataforma
        fields = ['nome']

class DesenvolvedoraForm(forms.ModelForm):
    class Meta:
        model = Desenvolvedora
        fields = ['nome']

class BibliotecaForm(forms.ModelForm):
    class Meta:
        model = Biblioteca
        fields = ['jogos']
        widgets = {
            'jogos': forms.CheckboxSelectMultiple
        }


class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['jogo', 'nota', 'comentario']
        widgets = {
            'comentario': forms.Textarea(attrs={'rows': 3}),
            'nota': forms.NumberInput(attrs={'min': 0, 'max': 10})
        }

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['amigo', 'jogo', 'data_emprestimo', 'data_devolucao']
        widgets = {
            'data_emprestimo': forms.DateInput(attrs={'type': 'date'}),
            'data_devolucao': forms.DateInput(attrs={'type': 'date'}),
        }

class NotificacaoForm(forms.ModelForm):
    class Meta:
        model = Notificacao
        fields = ['mensagem', 'lida']

