from django import forms
from django.core.exceptions import ValidationError

from ..models import User


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password']
    
    phone_number = forms.CharField(
        max_length=20,
        label='Telefone',
        error_messages={
            'max_length': 'Erro, número de telefone muito longo'
        },
        widget=forms.TextInput(attrs={'placeholder': 'Ex.: 75981041516', 'class': 'form-control'})
    )
    first_name = forms.CharField(
        max_length=150,
        label='Nome',
        error_messages={
            'max_length': 'Erro, nome muito longo'
        },
        widget=forms.TextInput(attrs={'placeholder': 'Ex.: Bruno...', 'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=150,
        label='Sobrenome',
        error_messages={
            'max_length': 'Erro, sobrenome muito longo'
        },
        widget=forms.TextInput(attrs={'placeholder': 'Ex.: Miranda...', 'class': 'form-control'})
    )

    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs={'placeholder': 'Ex.: joao@email.com', 'class': 'form-control'})
    )

    password = forms.CharField(
        max_length=150,
        label='Senha',
        error_messages={
            'max_length': 'Erro, senha é muito longa'
        },
        widget=forms.PasswordInput(attrs={'placeholder': 'Sua senha...', 'class': 'form-control'})
    )

    password2 = forms.CharField(
        max_length=150,
        label='Repita sua senha',
        error_messages={
            'max_length': 'Erro, sua senha é muito longa'
        },
        widget=forms.PasswordInput(attrs={'placeholder': 'Repita sua senha...', 'class': 'form-control'})
    )
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        
        if not phone_number:
            raise ValidationError('Erro, número de telefone é obrigatório')
        
        return phone_number
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        
        if len(password) < 4:
            raise ValidationError('Erro, Sua senha não pode ser menor que 4 caracteres')
        
        return password
    
    def clean_password2(self):
        password2 = self.cleaned_data.get('password2')
        
        if len(password2) < 4:
            raise ValidationError('Erro, Sua senha não pode ser menor que 4 caracteres')
        
        return password2
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not email:
            raise ValidationError('Erro, Email é obrigatório')
        
        email_exists = User.objects.filter(email=email).exists()
        if email_exists:
            raise ValidationError('Erro, email já cadastrado')
        
        return email
    
    def clean(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise ValidationError('Erro, as senhas não correspondem!')
        return super().clean()