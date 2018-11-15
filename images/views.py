from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import   I


#Create your views here
def index(request):
    title = 'Welcome to the most amazing social media app clone'
    return render(request, 'index.html',{"title": title})