from django.contrib.auth import authenticate, login
from django.shortcuts import HttpResponse, redirect, render
from django.views import View

from .forms.login_form import LoginForm
from .forms.register_form import RegisterForm


class RegisterView(View):
    """Class represents creation logic for new users"""
    def get(self, *args, **kwargs):

        if self.request.user.is_authenticated:
            return redirect('residences:dashboard')

        data_session = self.request.session.get('register_data')
        form = RegisterForm(data_session)
        return render(self.request, 'accounts/register.html', {'form': form})
    
    def post(self, *args, **kwargs):
        POST = self.request.POST
        self.request.session['register_data'] = POST
        
        form = RegisterForm(POST)
        
        if form.is_valid():

            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            
            del(self.request.session['register_data'])
            # messages.success(self.request, 'Usuário criado com sucesso!')

            return redirect('accounts:login')

        return redirect('accounts:register')


class LoginView(View):
    """Represents the login logic for users already registered"""
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('residences:dashboard')
        
        form = LoginForm()
        return render(self.request, 'accounts/login.html', {'form': form})
    
    def post(self, *args, **kwargs):
        form = LoginForm(self.request.POST)
        if form.is_valid():

            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(self.request, email=email, password=password)

            if user:
                login(self.request, user)
                return redirect('residences:dashboard')
        
        # messages.error(self.request, 'Nome de usuário e Senha não correspondem!')
        
        return redirect('accounts:login')