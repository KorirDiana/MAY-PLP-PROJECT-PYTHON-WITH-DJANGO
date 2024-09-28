from django.shortcuts import render

def home(request):
    return render(request, 'index.html')  # Ensure 'index.html' is in the correct template folder

def analysis(request):
    return render(request, 'analysis.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'register.html')