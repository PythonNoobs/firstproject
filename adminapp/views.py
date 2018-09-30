from django.shortcuts import render


def settings(request):
    pagename = 'Настройки'
    return render(request, 'adminapp/settings.html', {'pagename': pagename})


def access_rights(request):
    pagename = 'Права доступа'
    return render(request, 'adminapp/access_rights.html', {'pagename': pagename})
