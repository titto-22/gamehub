from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Jogo, Categoria, Plataforma, Desenvolvedora, Biblioteca, Avaliacao, Emprestimo, Notificacao, Favorito, Usuario
from .serializers import JogoSerializer, CategoriaSerializer, PlataformaSerializer, DesenvolvedoraSerializer
from django.shortcuts import render, get_object_or_404, redirect
from .forms import JogoForm, CategoriaForm, PlataformaForm, DesenvolvedoraForm, BibliotecaForm, AvaliacaoForm, EmprestimoForm, NotificacaoForm, FavoritoForm, UsuarioUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from .forms import UsuarioCreationForm
from .services import EmailSender


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'




class JogoViewSet(viewsets.ModelViewSet):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer
    permission_classes = [AllowAny]  

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

def jogo_list(request):
    jogos = Jogo.objects.all()
    return render(request, 'jogos/jogo_list.html', {'jogos': jogos})

def jogo_detail(request, pk):
    jogo = get_object_or_404(Jogo, pk=pk)
    return render(request, 'jogos/jogo_detail.html', {'jogo': jogo})

def jogo_create(request):
    if request.method == "POST":
        form = JogoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jogo_list')
    else:
        form = JogoForm()
    return render(request, 'jogos/jogo_form.html', {'form': form})

def jogo_update(request, pk):
    jogo = get_object_or_404(Jogo, pk=pk)
    if request.method == "POST":
        form = JogoForm(request.POST, instance=jogo)
        if form.is_valid():
            form.save()
            return redirect('jogo_list')
    else:
        form = JogoForm(instance=jogo)
    return render(request, 'jogos/jogo_form.html', {'form': form})

def jogo_delete(request, pk):
    jogo = get_object_or_404(Jogo, pk=pk)
    if request.method == "POST":
        jogo.delete()
        return redirect('jogo_list')
    return render(request, 'jogos/jogo_confirm_delete.html', {'jogo': jogo})



def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/categoria_list.html', {'categorias': categorias})

def categoria_detail(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    return render(request, 'categorias/categoria_detail.html', {'categoria': categoria})

def categoria_create(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria_list')
    else:
        form = CategoriaForm()
    return render(request, 'categorias/categoria_form.html', {'form': form})

def categoria_update(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categoria_list')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'categorias/categoria_form.html', {'form': form})

def categoria_delete(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == "POST":
        categoria.delete()
        return redirect('categoria_list')
    return render(request, 'categorias/categoria_confirm_delete.html', {'categoria': categoria})



def plataforma_list(request):
    plataformas = Plataforma.objects.all()
    return render(request, 'plataformas/plataforma_list.html', {'plataformas': plataformas})

def plataforma_detail(request, pk):
    plataforma = Plataforma.objects.get(pk=pk)
    return render(request, 'plataformas/plataforma_detail.html', {'plataforma': plataforma})

def plataforma_create(request):
    if request.method == 'POST':
        form = PlataformaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plataforma_list')
    else:
        form = PlataformaForm()
    return render(request, 'plataformas/plataforma_form.html', {'form': form})

def plataforma_update(request, pk):
    plataforma = Plataforma.objects.get(pk=pk)
    if request.method == 'POST':
        form = PlataformaForm(request.POST, instance=plataforma)
        if form.is_valid():
            form.save()
            return redirect('plataforma_list')
    else:
        form = PlataformaForm(instance=plataforma)
    return render(request, 'plataformas/plataforma_form.html', {'form': form})

def plataforma_delete(request, pk):
    plataforma = Plataforma.objects.get(pk=pk)
    if request.method == 'POST':
        plataforma.delete()
        return redirect('plataforma_list')
    return render(request, 'plataformas/plataforma_confirm_delete.html', {'plataforma': plataforma})



def desenvolvedora_list(request):
    desenvolvedoras = Desenvolvedora.objects.all()
    return render(request, 'desenvolvedoras/desenvolvedora_list.html', {'desenvolvedoras': desenvolvedoras})

def desenvolvedora_detail(request, pk):
    desenvolvedora = Desenvolvedora.objects.get(pk=pk)
    return render(request, 'desenvolvedoras/desenvolvedora_detail.html', {'desenvolvedora': desenvolvedora})

def desenvolvedora_create(request):
    if request.method == 'POST':
        form = DesenvolvedoraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('desenvolvedora_list')
    else:
        form = DesenvolvedoraForm()
    return render(request, 'desenvolvedoras/desenvolvedora_form.html', {'form': form})

def desenvolvedora_update(request, pk):
    desenvolvedora = Desenvolvedora.objects.get(pk=pk)
    if request.method == 'POST':
        form = DesenvolvedoraForm(request.POST, instance=desenvolvedora)
        if form.is_valid():
            form.save()
            return redirect('desenvolvedora_list')
    else:
        form = DesenvolvedoraForm(instance=desenvolvedora)
    return render(request, 'desenvolvedoras/desenvolvedora_form.html', {'form': form})

def desenvolvedora_delete(request, pk):
    desenvolvedora = Desenvolvedora.objects.get(pk=pk)
    if request.method == 'POST':
        desenvolvedora.delete()
        return redirect('desenvolvedora_list')
    return render(request, 'desenvolvedoras/desenvolvedora_confirm_delete.html', {'desenvolvedora': desenvolvedora})


@login_required
def biblioteca_list(request):
    bibliotecas = Biblioteca.objects.filter(usuario=request.user)  # Filtrar bibliotecas do usuário autenticado
    return render(request, 'bibliotecas/biblioteca_list.html', {'bibliotecas': bibliotecas})

@login_required
def biblioteca_detail(request, pk):
    biblioteca = Biblioteca.objects.get(pk=pk, usuario=request.user)
    return render(request, 'bibliotecas/biblioteca_detail.html', {'biblioteca': biblioteca})

@login_required
def biblioteca_create(request):
    if request.method == 'POST':
        form = BibliotecaForm(request.POST)
        if form.is_valid():
            biblioteca = form.save(commit=False)
            biblioteca.usuario = request.user
            biblioteca.save()
            form.save_m2m()
            return redirect('biblioteca_list')
    else:
        form = BibliotecaForm()
    return render(request, 'bibliotecas/biblioteca_form.html', {'form': form})

@login_required
def biblioteca_update(request, pk):
    biblioteca = get_object_or_404(Biblioteca, pk=pk, usuario=request.user)  
    if request.method == 'POST':
        form = BibliotecaForm(request.POST, instance=biblioteca)
        if form.is_valid():
            form.save()
            return redirect('biblioteca_list')
    else:
        form = BibliotecaForm(instance=biblioteca)
    return render(request, 'bibliotecas/biblioteca_form.html', {'form': form})

@login_required
def biblioteca_delete(request, pk):
    biblioteca = Biblioteca.objects.get(pk=pk, usuario=request.user)
    if request.method == 'POST':
        biblioteca.delete()
        return redirect('biblioteca_list')
    return render(request, 'bibliotecas/biblioteca_confirm_delete.html', {'biblioteca': biblioteca})




@login_required
def avaliacao_list(request):
    avaliacoes = Avaliacao.objects.all()
    return render(request, 'avaliacoes/avaliacao_list.html', {'avaliacoes': avaliacoes})

@login_required
def avaliacao_create(request):
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            avaliacao = form.save(commit=False)
            avaliacao.usuario = request.user
            avaliacao.save()
            return redirect('avaliacao_list')
    else:
        form = AvaliacaoForm()
    return render(request, 'avaliacoes/avaliacao_form.html', {'form': form})

@login_required
def avaliacao_update(request, pk):
    avaliacao = Avaliacao.objects.get(pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST, instance=avaliacao)
        if form.is_valid():
            form.save()
            return redirect('avaliacao_list')
    else:
        form = AvaliacaoForm(instance=avaliacao)
    return render(request, 'avaliacoes/avaliacao_form.html', {'form': form})

@login_required
def avaliacao_delete(request, pk):
    avaliacao = Avaliacao.objects.get(pk=pk, usuario=request.user)
    if request.method == 'POST':
        avaliacao.delete()
        return redirect('avaliacao_list')
    return render(request, 'avaliacoes/avaliacao_confirm_delete.html', {'avaliacao': avaliacao})




@login_required
def emprestimo_list(request):
    emprestimos = Emprestimo.objects.filter(dono=request.user)
    return render(request, 'emprestimos/emprestimo_list.html', {'emprestimos': emprestimos})

@login_required
def emprestimo_create(request):
    if request.method == 'POST':
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            emprestimo = form.save(commit=False)
            if emprestimo.amigo == request.user:  # Verifica se o usuário está tentando emprestar para si mesmo
                form.add_error('amigo', 'Você não pode emprestar jogos para si mesmo.')
            else:
                emprestimo.dono = request.user
                emprestimo.save()
                return redirect('emprestimo_list')
    else:
        form = EmprestimoForm()
    return render(request, 'emprestimos/emprestimo_form.html', {'form': form})

@login_required
def emprestimo_update(request, pk):
    emprestimo = Emprestimo.objects.get(pk=pk, dono=request.user)
    if request.method == 'POST':
        form = EmprestimoForm(request.POST, instance=emprestimo)
        if form.is_valid():
            form.save()
            return redirect('emprestimo_list')
    else:
        form = EmprestimoForm(instance=emprestimo)
    return render(request, 'emprestimos/emprestimo_form.html', {'form': form})

@login_required
def emprestimo_delete(request, pk):
    emprestimo = Emprestimo.objects.get(pk=pk, dono=request.user)
    if request.method == 'POST':
        emprestimo.delete()
        return redirect('emprestimo_list')
    return render(request, 'emprestimos/emprestimo_confirm_delete.html', {'emprestimo': emprestimo})


@login_required
def notificacao_list(request):
    notificacoes = Notificacao.objects.filter(usuario=request.user)
    return render(request, 'notificacoes/notificacao_list.html', {'notificacoes': notificacoes})

@login_required
def notificacao_create(request):
    if request.method == 'POST':
        form = NotificacaoForm(request.POST)
        if form.is_valid():
            notificacao = form.save(commit=False)
            notificacao.usuario = request.user
            notificacao.save()
            EmailSender().enviar(notificacao.destinatario.email, notificacao.mensagem)
            return redirect('notificacao_list')
    else:
        form = NotificacaoForm()
    return render(request, 'notificacoes/notificacao_form.html', {'form': form})

@login_required
def notificacao_update(request, pk):
    notificacao = Notificacao.objects.get(pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = NotificacaoForm(request.POST, instance=notificacao)
        if form.is_valid():
            form.save()
            return redirect('notificacao_list')
    else:
        form = NotificacaoForm(instance=notificacao)
    return render(request, 'notificacoes/notificacao_form.html', {'form': form})

@login_required
def notificacao_delete(request, pk):
    notificacao = Notificacao.objects.get(pk=pk, usuario=request.user)
    if request.method == 'POST':
        notificacao.delete()
        return redirect('notificacao_list')
    return render(request, 'notificacoes/notificacao_confirm_delete.html', {'notificacao': notificacao})




@login_required
def favorito_list(request):
    favoritos = Favorito.objects.filter(usuario=request.user)
    return render(request, 'favoritos/favorito_list.html', {'favoritos': favoritos})

@login_required
def favorito_create(request):
    if request.method == 'POST':
        form = FavoritoForm(request.POST)
        if form.is_valid():
            favorito = form.save(commit=False)
            favorito.usuario = request.user
            favorito.save()
            return redirect('favorito_list')
    else:
        form = FavoritoForm()
    return render(request, 'favoritos/favorito_form.html', {'form': form})

@login_required
def favorito_delete(request, pk):
    favorito = Favorito.objects.get(pk=pk, usuario=request.user)
    if request.method == 'POST':
        favorito.delete()
        return redirect('favorito_list')
    return render(request, 'favoritos/favorito_confirm_delete.html', {'favorito': favorito})


Usuario = get_user_model()

@login_required
def usuario_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/usuario_list.html', {'usuarios': usuarios})

@login_required
def usuario_create(request):
    if request.method == "POST":
        form = UsuarioCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuario_list')
    else:
        form = UsuarioCreationForm()
    return render(request, 'usuarios/usuario_form.html', {'form': form})

@login_required
def usuario_update(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == "POST":
        form = UsuarioUpdateForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuario_list')
    else:
        form = UsuarioUpdateForm(instance=usuario)
    return render(request, 'usuarios/usuario_form.html', {'form': form})

@login_required
def usuario_delete(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == "POST":
        usuario.delete()
        return redirect('usuario_list')
    return render(request, 'usuarios/usuario_confirm_delete.html', {'usuario': usuario})

def home_page(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UsuarioCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            print(form.errors) 
    else:
        form = UsuarioCreationForm()
    return render(request, 'accounts/register.html', {'form': form})