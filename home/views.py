from django.shortcuts import render
from django.contrib.auth import login, authenticate
from .forms import CustomSignUpForm
from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def signup_view(request):
    form = CustomSignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        date_of_birth = form.cleaned_data.get('date_of_birth')
        user = authenticate(username=username, password=password, date_of_birth=date_of_birth)
        login(request, user)
        return redirect('home')
    else:
        form = CustomSignUpForm()
    return render(request, 'signup.html', {'form': form})