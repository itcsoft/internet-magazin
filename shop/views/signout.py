from django.shortcuts import render
from django.contrib.auth import logout

def signout(request):
    logout(request)

    return render(request, 'index.html')