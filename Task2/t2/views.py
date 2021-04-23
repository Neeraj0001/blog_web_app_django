from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib import messages
from .forms import CreateUserForm, profile_form, post_all_form
from .models import Profile, Post_all, Post_public, Post_private
from .decorator import allowed_user, admin_only
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('True')
            login(request, user)

            place = Profile.objects.get(user=user)

            print(place)
            x = str(place.id)
            print(x)
            return redirect('../user/'+x+'/')
        else:
            messages.info(request, 'Usernaame Or Password is not correct')
    context = {}
    return render(request, 'login.html', context)


def registration(request):
    form = CreateUserForm()
    if request.method == 'POST':
        print(request.POST)
        form = CreateUserForm(request.POST)
        if form.is_valid():

            user = form.save()

            username = form.cleaned_data.get('username')
            Profile.objects.create(
                user=user
            )
            messages.success(
                request, "Account Successfully created of "+username)
            return redirect('../login/')

    context = {'form': form}
    return render(request, 'registration.html', context)


@login_required(login_url='login')
def user_form(request):
    user = request.user.profile

    form = profile_form(instance=user)
    print(form)
    if request.method == 'POST':
        user = request.user.profile
        Profile.objects.create(
            user=user
        )
        form = profile_form(request.POST, request.FILES, instance=user)
        if form.is_valid():

            form.save()

            x = str(request.user.profile.id)
            return redirect('../user/'+x+'/')
    context = {'form': form}
    return render(request, 'update_form.html', context)


@login_required(login_url='login')
def user(request, pk_test):
    pk_test = int(pk_test)
    profile = Profile.objects.get(id=pk_test)
    print(request.user)
    posts = Post_all.objects.filter(user=request.user)
    print(posts)
    if request.method == "POST":
        form = post_all_form(
            data=request.POST, files=request.FILES)

        if form.is_valid():

            candidate = form.save(commit=False)

            candidate.user = request.user  # use your own profile here
                
            candidate.save()
        
    else:
        form = post_all_form()
        

    context = {'profile': profile, 'form': form, 'posts': posts}
    return render(request, 'user_dashboard.html', context)


def logoutUser(request):
    logout(request)
    return redirect('../login/')
def search(request):
    if request.method=="POST":
        name=request.POST.get('name')
        pk=User.objects.get(username=name).pk
        posts = Post_all.objects.filter(user=pk,Mode='public')
        print(posts)
        context={'posts':posts}
    return render(request, 'search.html', context)
