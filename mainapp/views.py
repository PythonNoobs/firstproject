from django.shortcuts import render

# сreate your views here.


def main(request):
    pagename = 'Главная'
    return render(request, 'main.html', {'pagename': pagename})
