from django.shortcuts import render
from django.http import HttpResponse
from django.template.context_processors import request
from django.views.generic import ListView, DetailView
from .models import *
from django.urls import reverse_lazy
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.urls import reverse
from django.contrib.auth.decorators import login_required



def home(request):
    context = {}
    context['user'] = request.user
    return render(request, 'home.html',context)


def gallery(request):
    context = {}
    context['user'] = request.user
    return render(request, 'gallery.html',context)


def blog(request):
    context = {}
    context['user'] = request.user
    return render(request, 'blog.html',context)


def about(request):
    context = {}
    context['user'] = request.user
    return render(request, 'about.html',context)

@login_required(login_url="home")
def pure(request):
    context = {}
    context['user'] = request.user
    context['upcoming_classes'] = Upcoming_Classes.objects.filter()
    return render(request, 'pure.html',context)


def upcoming_class(request):
    context = {}
    context['upcoming_classes'] = Upcoming_Classes.objects.filter()
    return render(request, 'upcoming_classes.html',context)


def semi(request):
    context = {}
    context['user'] = request.user
    return render(request, 'semi.html',context)


def Bharatanatyam(request):
    context = {}
    context['user'] = request.user
    return render(request,'Bharatanatyam.html',context)



def prarambhik(request):
    context = {}
    context['user'] = request.user
    return render(request,'prarambhik.html',context)


def feedback(request):
 
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phoneNo=request.POST.get("num")
        feedback=request.POST.get("feedback")
        stars=request.POST.get("stars")
        info_var=Feedbacks(name=name,email=email,phoneNo=phoneNo,feedback=feedback,stars=stars)
        info_var.save()
        return render(request, 'feedback.html')

    else:
        return render(request, 'feedback.html')
        

def signup(request):
    context = {}

    if request.method == 'POST':
        name = request.POST['Form-name']
        username = request.POST['Form-username']
        email = request.POST['Form-email1']
        pass1 = request.POST['Form-pass1']
        pass2 = request.POST['Form-pass2']

        if User.objects.filter(username=username).exists():
            messages.info(request,'Username taken')
            return redirect('home')

        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email taken')
            return redirect('home')

        else:
            if pass1 == pass2:
                user = User.objects.create_user(username=username, password=pass1, email=email, first_name=name)
                user.save()
                user1 = auth.authenticate(username=username,password=pass1)
                if user1 is not None:
                    auth.login(request,user1)
                    return render(request,'home.html',context)
                


def login(request):
    context = {}

    if request.method == 'POST':
        username = request.POST['Form-usernamelogin']
        passw = request.POST['Form-passlogin1']

        user = auth.authenticate(username=username,password=passw)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.info(request,'Invalid credentials')
            return redirect('home')
    else:
        return render(request,'login.html',context)


def logout(request):
    auth.logout(request)
    return redirect('/')


def classes(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phoneNo=request.POST.get("num")
        experience=request.POST.get("experience")
        info_var=Classes(name=name,email=email,phoneNo=phoneNo,experience=experience)
        info_var.save()
        return render(request, 'classes.html')

    else:
        return render(request, 'classes.html')
