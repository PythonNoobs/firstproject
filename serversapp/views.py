from django.shortcuts import render


def list_servers(request):
    pagename = 'Все'
    return render(request, 'serversapp/list_servers.html', {'pagename': pagename})


def add_server(request):
    pagename = 'Новый сервер'
    return render(request, 'serversapp/add_server.html', {'pagename': pagename})


def edit_server(request):
    pagename = 'Изменить данные сервера'
    return render(request, 'serversapp/edit_server.html', {'pagename': pagename})
