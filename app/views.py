# Create your views here.

from django.shortcuts import get_object_or_404, redirect, render 
from django.contrib.auth import authenticate, logout, login 
from django.contrib.auth.decorators import login_required  
from django.contrib.auth.models import User 
from .models import Acessorio, Item  

def index(request):  
    return render(request, 'index.html')  

def cadastro(request): 
    if request.method == 'POST': 
        username = request.POST.get('username') 
        password = request.POST.get('password')  
        User.objects.create_user(username=username, password=password) 
        return redirect('entrar') 
    return render(request, 'cadastro.html')  

def entrar(request): 
    if request.method == 'POST': 
        username = request.POST.get('username') 
        password = request.POST.get('password')  
        usuario = authenticate(request, username=username, password=password) 
        if usuario:   
            login(request, usuario)   
            return redirect('listar')   
    return render(request, 'login.html')    

def sair(request):   
    logout(request) 
    return redirect('index')  

@login_required 
def listar(request):  
    itens = Item.objects.filter(usuario=request.user)  
    return render(request, 'listar.html', {'itens': itens})  

@login_required    
def criar(request):   
    if request.method == 'POST': 
        nome = request.POST.get('nome') 
        if nome:  
            Item.objects.create(nome=nome, usuario=request.user)   
            return redirect('listar')  
    return render(request, 'criar.html')    

@login_required 
def editar(request, id):   
    item = get_object_or_404(Item, id=id, usuario=request.user)     
    if request.method == 'POST':   
        nome = request.POST.get('nome') 
        if nome:  
            item.nome = nome 
            item.save() 
            return redirect('listar')   
    return render(request, 'editar.html', {'item': item})   

@login_required  
def excluir(request, id):     
    item = get_object_or_404(Item, id=id, usuario=request.user)   
    if request.method == 'POST':   
        item.delete() 
        return redirect('listar')   
    return render(request, 'excluir.html', {'item': item})     

@login_required 
def listarr(request, id):  
    item = get_object_or_404(Item, id=id, usuario=request.user)  
    acessorios = Acessorio.objects.filter(item=item)    
    return render(request, 'listarr.html', {'item': item, 'acessorios': acessorios})   

@login_required 
def criarr(request, id):   
    item = get_object_or_404(Item, id=id, usuario=request.user)   
    if request.method == 'POST':  
        nome = request.POST.get('nome')    
        if nome:   
            Acessorio.objects.create(nome=nome, item=item)  
            return redirect('listarr', id=item.id)    
    return render(request, 'criarr.html', {'item': item})   

@login_required 
def editarr(request, id):   
    acessorio = get_object_or_404(Acessorio, id=id, item__usuario=request.user)   
    if request.method == 'POST': 
        nome = request.POST.get('nome')   
        if nome:  
            acessorio.nome = nome 
            acessorio.save() 
            return redirect('listarr', id=acessorio.item.id)  
    return render(request, 'editarr.html', {'acessorio': acessorio})     

@login_required 
def excluirr(request, id):   
    acessorio = get_object_or_404(Acessorio, id=id, item__usuario=request.user)   
    if request.method == 'POST':  
        acessorio.delete()  
        return redirect('listarr', id=acessorio.item.id)     
    return render(request, 'excluirr.html', {'acessorio': acessorio})    

