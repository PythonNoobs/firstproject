from django.shortcuts import render
from .models import Server


def list_servers(request):
    servers = Server.objects.all()
    return render(request, 'serversapp/list_servers.html', {'servers': servers})


def add_server(request):
    pagename = 'Новый сервер'
    return render(request, 'serversapp/add_server.html', {'pagename': pagename})


def edit_server(request):
    pagename = 'Изменить данные сервера'
    return render(request, 'serversapp/edit_server.html', {'pagename': pagename})
