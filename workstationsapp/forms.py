from django import forms


class ExcelForm(forms.Form):

    file = forms.FileField(label= "Выберите excel файл для загрузки")