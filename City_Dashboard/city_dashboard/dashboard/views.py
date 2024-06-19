from django.shortcuts import render

def index(request):
  
    return render(request, 'dashboard/index.html')

def SignUp(request):

    return render(request, 'dashboard/SignUp.html')