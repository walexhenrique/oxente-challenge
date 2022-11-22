from django import forms


class LoginForm(forms.Form):
    class Meta:
        fields = ('email', 'password')
    
    email = forms.EmailField(
        label='E-mail',
        error_messages={
            'max_length': 'Credenciais inválidas',
        },
        widget=forms.EmailInput(attrs={'placeholder': 'Ex.: joao@email.com'})
    )

    password = forms.CharField(
        max_length=150,
        label='Senha',
        error_messages={
            'max_length': 'Credenciais inválidas',
        },
        widget=forms.PasswordInput(attrs={'placeholder': 'Senha...'})
    )
