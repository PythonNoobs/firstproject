from django.shortcuts import render


def list_tickets(request):
    pagename = 'Все'
    return render(request, 'ticketsapp/list_tickets.html', {'pagename': pagename})


def add_ticket(request):
    pagename = 'Новая заявка'
    return render(request, 'ticketsapp/add_ticket.html', {'pagename': pagename})


def edit_ticket(request):
    pagename = 'Изменить заявку'
    return render(request, 'ticketsapp/edit_ticket.html', {'pagename': pagename})
