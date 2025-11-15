from django import forms
from . import models
from hashlib import sha512


class RegistrationForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        label='Логин',
        widget=forms.TextInput(attrs={'placeholder': 'Логин'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'})
    )
    password_confirm = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Подтверждение пароля'})
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if len(username) < 2:
            raise forms.ValidationError(
                "Имя должно содержать минимум 2 символа")

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if models.Member.objects.filter(email=email).exists():
            raise forms.ValidationError("Данная почта уже используется")

        return email

    def clean_password(self):
        password: str = self.cleaned_data.get('password')
        password = password.encode('utf8')
        return str(sha512(password).digest())

    def clean_password_confirm(self):
        if self.data.get('password') != self.data.get('password_confirm'):
            raise forms.ValidationError("Пароли не совпадают")
        return True


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        label='Логин',
        widget=forms.TextInput(attrs={'placeholder': 'Логин'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'})
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 2:
            raise forms.ValidationError(
                "Имя должно содержать минимум 2 символа")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not models.Member.objects.filter(email=email).exists():
            raise forms.ValidationError("Данная почта нам не знакома")

        return email

    def clean_password(self):
        password: str = self.cleaned_data.get('password')
        password = password.encode('utf8')
        return str(sha512(password).digest())


class FeedbackForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        label='Логин',
        widget=forms.TextInput(attrs={'placeholder': 'Логин'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )
    topic = forms.CharField(
        label='Тема сообщения',
        widget=forms.PasswordInput(attrs={'placeholder': 'Тема сообщения'})
    )
    text = forms.CharField(
        label='Текст сообщения',
        min_length=10,
        max_length=300,
        widget=forms.Textarea(attrs={'placeholder': 'Текст сообщения'})
    )
