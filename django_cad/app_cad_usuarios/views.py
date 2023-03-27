from django.shortcuts import render

from .models import Usuario


# Create your views here.
def home(request):
    return render(request, 'usuarios/home.html')

def add_user(request):
    # Salvar os dados da tela para po banco de dados
    new_user = Usuario()
    new_user.nome_usuario = request.POST.get('name_user')
    new_user.idade_usuario = request.POST.get('age_user')
    new_user.save()
    # Exibir todos os usuários já cadastrados em uma nova página
    dict_usuarios = {
        'usuarios':Usuario.objects.all()
    }
    # Retornar os dados para a página de listagem de usuários
    return render(request, 'usuarios/usuarios.html', dict_usuarios)