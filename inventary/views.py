from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def signin(request):
    return render(request, 'signin.html')

def signup(request):
    return render(request, 'signup.html')

def entry(request):
    return render(request, 'entry.html')

def inventary(request):
    return render(request, 'inventary.html')

def sell(request):
    return render(request, 'sell.html')