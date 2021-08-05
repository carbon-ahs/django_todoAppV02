from django.shortcuts import render, redirect

'''
from .models import 
from .forms import 
'''
app_name = 't_app'

def home(request):
    contex = {
        'key': 'value',
    }
    return render(request, 'home.html', contex)



def about(request):
    contex = {
        'key': 'value',
    }
    return render(request, 'about.html', contex)

def tempu(request):
    header = 'TEMPU VRUMMMM'

    contex = {
        'header' : header,
        'key': 'value',
        'app_name' : app_name,
    }
    return render(request, 'tempu.html', contex)