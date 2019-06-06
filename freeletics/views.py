from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, 'index.html',)
