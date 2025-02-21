from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from .forms import EmailLoginForm

def user_login(request):
    if request.method == 'POST':
        form = EmailLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            
            # Get username from email
            try:
                user = User.objects.get(email=email)
                # Now authenticate with username
                user = authenticate(username=user.username, password=password)
                if user is not None:
                    auth_login(request, user)
                    return redirect('home')
            except User.DoesNotExist:
                pass
            
            form.add_error(None, "Invalid email or password")
    else:
        form = EmailLoginForm()
    
    return render(request, "login/login.html", {'form': form})


def user_logout(request):
    logout(request)

    return redirect("home")
