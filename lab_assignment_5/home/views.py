from django.shortcuts import render
from django.http import HttpResponse
import home

# Create your views here.

def show(self):
    return render(self, 'message.html')