from django.shortcuts import render
from django.http import HttpResponse
from .models import data
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect



def home(request):
    return  render (request, 'usuarios/index.html')


#para salvar os dados da tela para o banco de dados
def dados(request):
    if request.method == 'POST':
        novo_usuario = data()
        novo_usuario.rm = int(request.POST.get('rm'))
        novo_usuario.celular = int(request.POST.get('celular'))
        novo_usuario.nome = request.POST.get('nome') 
        novo_usuario.idade = int(request.POST.get('idade'))
        novo_usuario.save()
        return redirect('dados_usuarios')
    
    #exibir os dados dos usuarios em uma nova tela

    dados = {
     'dados': data.objects.all()
    }

    #retornar os dados para a pagina de listagem

    return render(request, 'usuarios/dados.html' , dados)


