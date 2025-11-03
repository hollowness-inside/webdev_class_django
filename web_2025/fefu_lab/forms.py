from django import forms


def clean_name(self):
    name = self.cleaned_data['name']
    if len(name.strip()) < 2:
        raise forms.ValidationError("Имя должно содержать минимум 2 символа")
    return name.strip()


class RegistrationForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        label='Логин',
        validators=[clean_name],
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


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        label='Логин',
        validators=[clean_name],
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
