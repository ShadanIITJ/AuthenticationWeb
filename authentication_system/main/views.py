from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import *
from .models import *
# Create your views here.
def auth_login(request):
    m=''
    if(request.user.is_authenticated):
        return redirect('main_view')

    if(request.method=='POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('main_view')
        else:
            m="Wrong user name or Password"
    form = AuthenticationForm()
    return render(request, 'main/login.html',{'form':form,'message':m})

def main_view(request):
    if(request.user.is_authenticated):
        if(request.user.is_superuser):
            message=''
            assigned = student.objects.all().order_by('-deadline')
            if(request.method=='POST'):
                form = taskform(request.POST)
                if(form.is_valid()):
                    n = form['name'].value()
                    try:
                        check = User.objects.get(username=n)
                        if(check==request.user):
                            message = f"Student, {n} Does't exist"
                        else:
                            form.save()
                            return redirect('main_view')
                    except:
                        message = f"Student, {n} Does't exist"
                else:
                    return render(request, 'main/admin.html' ,{'form':form,'assigned':assigned, 'message':message})


            form = taskform()
            return render(request, 'main/admin.html' ,{'form':form,'assigned':assigned,'message':message})
        else:
            assigned = student.objects.filter(name=request.user.username).order_by('deadline')
            return render(request, 'main/student.html' ,{'assigned':assigned})
    return redirect('login')

def lout(request):
    logout(request)
    return redirect('login')
    