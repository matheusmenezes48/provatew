from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required



def home(request):
    return render(request, 'home.html',{})
@login_required
def list(request):
    users = User.objects.all()
    return render (request,'list.html',{'users':users})

@permission_required("user_delete")
def user_delete(request, id):
    user = User.objects.get(pk=id)
    user.delete()
    return redirect("/home/list/")

