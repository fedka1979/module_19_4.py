from django import forms


class UserRegister(forms.Form):
    username = forms.CharField(
        label="Введите логин",
        max_length=30,
        widget=forms.TextInput(attrs={"placeholder": "Введите логин"}),
    )
    password = forms.CharField(
        label="Введите пароль",
        min_length=8,
        widget=forms.PasswordInput(attrs={"placeholder": "Введите пароль"}),
    )
    repeat_password = forms.CharField(
        label="Повторите пароль",
        min_length=8,
        widget=forms.PasswordInput(attrs={"placeholder": "Повторите пароль"}),
    )
    age = forms.CharField(
        label="Введите свой возраст",
        max_length=3,
        widget=forms.NumberInput(attrs={"placeholder": "Введите свой возраст"}),
    )