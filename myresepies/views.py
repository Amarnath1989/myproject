# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# python Imports

# Third party Imports


# Rest imports

# Django imports
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

# other apps

# local imports
from myresepies.models import Resepi


# Create your views here.


def login_view(request):
    """ If user is loged in proceeds further else display login page"""
    if request.user.is_authenticated():
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            # correct username and password login the user
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Error wrong username/password')
    return render(request, 'myresepies/login.html')


def logout_view(request):
    """ logging out the user from the session"""
    logout(request)
    return redirect('login')


def user_creation(request):
    """ Creating New USers to the User object of Authentication"""
    if request.method == 'POST':
        user_name = request.POST['username']
        email = request.POST['email']
        password = request.POST['pwd']
        User.objects.create_user(user_name, email, password)
        return HttpResponseRedirect(reverse('login', args=()))
    return render(request, 'myresepies/create_user.html', {})


@login_required
def index(request):
    """ Display all the Resepies from the Resepi Model """
    resepies_list = Resepi.objects.all()
    context = {'resepies_list': resepies_list}
    return render(request, 'myresepies/index.html', context)


@login_required
def detail(request, id):
    """ Display all the details of specified Resepi """
    resipies_list = Resepi.objects.get(id=id)
    # import ipdb; ipdb.set_trace()
    context = {'resipies_list': resipies_list}
    return render(request, 'myresepies/details.html', context)


@login_required
def create_resepi(request):
    """ Create new resepi"""
    if request.method == 'POST':
        Resepi.objects.create(name=request.POST['name'],
                              ingredients=request.POST['ingredients'],
                              process=request.POST['process'],
                              image=request.POST['img'],
                              created_by=request.user.username
                              )
        return HttpResponseRedirect(reverse('index', args=()))
    return render(request, 'myresepies/create.html', {})


def delete_resepi(request, resepi_id):
    resepi = Resepi.objects.get(id=resepi_id)
    resepi.delete()
    return redirect('index')
