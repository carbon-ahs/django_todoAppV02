from django.shortcuts import render, redirect

'''
from .models import 
from .forms import 
'''
def home(request):

    contex = {
        'key': 'value',
    }
    return render(request, 'home.html', contex)