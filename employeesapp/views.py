from django.shortcuts import render


def list_employees(request):
    pagename = 'Все'
    return render(request, 'employeesapp/list_employees.html', {'pagename': pagename})


def add_employee(request):
    pagename = 'Новый сотрудник'
    return render(request, 'employeesapp/add_employee.html', {'pagename': pagename})


def edit_employee(request):
    pagename = 'Изменить данные сотрудника'
    return render(request, 'employeesapp/edit_employee.html', {'pagename': pagename})


def telephone_book(request):
    pagename = 'Телефонный справочник'
    return render(request, 'employeesapp/telephone_book.html', {'pagename': pagename})


def birthdays(request):
    pagename = 'Дни рождения сотрудников'
    return render(request, 'employeesapp/birthdays.html', {'pagename': pagename})
