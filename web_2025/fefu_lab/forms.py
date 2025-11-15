from django import forms


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
