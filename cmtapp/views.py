from django.shortcuts import render


def list_cmts(request):
    pagename = 'Все'
    return render(request, 'cmtapp/list_cmt.html', {'pagename': pagename})


def add_cmt(request):
    pagename = 'Новая КМТ'
    return render(request, 'cmtapp/add_cmt.html', {'pagename': pagename})


def edit_cmt(request):
    pagename = 'Изменить данные КМТ'
    return render(request, 'cmtapp/edit_cmt.html', {'pagename': pagename})
