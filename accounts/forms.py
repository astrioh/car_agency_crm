from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.forms import ModelChoiceField
from django.contrib.auth.forms import AuthenticationForm, UsernameField

from employees.models import Role, genders

User = get_user_model()

class DateInput(forms.DateInput):
    input_type = 'date'


class RoleModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.full_name


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label=("Логин"),
        strip=False,
        widget=forms.TextInput(),
    )

    password1 = forms.CharField(
        label=("Пароль"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )

    password2 = forms.CharField(
        label=("Подтвердите пароль"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )

    last_name = forms.CharField(max_length=30, label='Фамилия')
    first_name = forms.CharField(max_length=30, label='Имя')
    middle_name = forms.CharField(max_length=30, label='Отчество')
    sex = forms.CharField(max_length=10, label='Пол', widget=forms.Select(choices=genders))
    birthday = forms.DateField(widget=DateInput, label='Дата рождения')
    pass_series = forms.CharField(max_length=5, label='Серия паспорта')
    pass_number = forms.CharField(max_length=10, label='Номер паспорта')
    inn = forms.CharField(max_length=15, required=False, label='ИНН')
    email = forms.CharField(max_length=30, label='E-mail')
    address = forms.CharField(max_length=80, required=False, label='Адрес')
    phone = forms.CharField(max_length=20, label='Телефон')
    role = RoleModelChoiceField(queryset=Role.objects.all(), empty_label=None, label='Роль')

    class Meta:
        model = User
        
        fields = ('username',)

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True}), label="Логин")
    password = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )