from django.shortcuts import render, redirect

from .forms import UserRegistrationForm, RealtorRegistrationForm

# Create your views here.
def user_registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/home_buyers.html', {'form': form})


def realtor_registration(request):
    if request.method == 'POST':
        form = RealtorRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = RealtorRegistrationForm()
    
    return render(request, 'registration/realtors.html', {'form': form})


def type_user_redirect(request):
    return render(request, 'registration/redirect_question.html', {})

