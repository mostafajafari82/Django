from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SingUpForm
from django. http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib import messages

def LoginView(request):
    next_url = request.GET.get('next', '')
    
    messages.info(request, "برای دیدن صفحه ها باید لاگین کنید")
    if request.method == "POST": 
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                if next_url:
                    return HttpResponseRedirect(next_url)
                else:
                    return redirect('home')
            else:
                messages.error(request, "invalid username or password")
    else:
        form = LoginForm()
        
    return render(request, 'registration/login.html', {'form': form, 'next': next_url})
    

def LogoutView(request):
    logout(request)
    return redirect('home') 


def SingUpView(request):
    if request.method == 'POST':
        form = SingUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)  
            return redirect('home')
    else:
        form = SingUpForm()
    return render(request, 'registration/singup.html', {'form': form})
