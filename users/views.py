from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.

class LoginView(View):
    def get(self,request):
        login_form = LoginForm
        context = {
            'login_form':login_form
        }
        return render(request,'users/login.html', context)
    
    
    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
                
            else:
                form.add_error(None,'fudsfgisudgb')
            
        return render(request, 'users/login.html', {'form':form})
    
    
class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('homepage')
        