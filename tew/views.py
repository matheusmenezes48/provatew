from django.shortcuts import render
from django.contrib.auth.models import User


def home(request):
    return render(request, 'home.html',{})

def list(request):
    users = User.objects.all()
    return render (request,'list.html',{'users':users})

def user_delete(request,id):
    user = User.objects.get(pk=id)
    user.delete()
    return render(request,'list.html')