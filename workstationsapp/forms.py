from django import forms
from django.forms import ModelForm
from .models import Computer


class ExcelForm(forms.Form):

    file = forms.FileField(label= "Выберите excel файл для загрузки")


class ComputerForm(ModelForm):
    class Meta:
        model = Computer
        fields = (
            'inventorynum',
            'serialnum',
            'name',
            'netbiosname',
            'ip',
            'macaddress',
            'computermodel_id',
        )
        labels = {
            'inventorynum': 'Инвентарный номер',
            'serialnum': 'Серийный номер',
            'name': 'Имя компьютера',
            'netbiosname': 'NETBIOS-имя',
            'ip': 'IP-адрес',
            'macaddress': 'MAC-адрес',
            'computermodel_id': 'Модель'
        }
        widgets = {
            'inventorynum': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Инвентарный номер'}),
            'serialnum': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Серийный номер'}),
            'name': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'Имя компьютера'}),
            'netbiosname': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'NETBIOS-имя'}),
            'ip': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'IP-адрес'}),
            'macaddress': forms.TextInput(attrs={
                'class': 'form-control', 'placeholder': 'MAC-адрес'}),
            'computermodel_id': forms.Select(attrs={
                'class': 'form-control form-control', 'type': 'text'}),
        }