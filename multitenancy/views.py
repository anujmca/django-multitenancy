from django.contrib.auth import login as django_login, logout as django_logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.db import connection
from sweet_tenant.views import public_createuser as p_createuser, public_add_certificate as p_add_certificate, \
    Certificate


# Create your views here.

def home(request):
    if not request.user.is_authenticated or request.user.is_anonymous:
        return render(request, 'login.html', None)
    else:
        return redirect('/index')


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = User.objects.get(username=username)
    if user:
        if user.check_password(password):
            django_login(request=request, user=user)

    return redirect('/index')


def logout(request):
    if request.user.is_authenticated and not request.user.is_anonymous:
        django_logout(request)

    return redirect('/')


def index(request):
    if not request.user.is_authenticated or request.user.is_anonymous:
        return redirect('/login')
    else:
        schema_name = connection.schema_name
        return render(request, 'index.html', context={'schema_name': schema_name})


def public_createuser(request):
    user = p_createuser(request)

    return render(request, 'index.html', context={'created': True, 'user': user})


def public_create_certificate(request):
    public_username = request.POST['public_username']
    certificate_name = request.POST['certificate_name']
    certificate = p_add_certificate(request=request, user_name=public_username, certificate_name=certificate_name)
    return render(request, 'index.html', context={'created': True, 'certificate': certificate})


def public_mycertificates(request):
    certificates = Certificate.objects.filter(awardee=request.user)
    return render(request, 'mycertificates.html', context={'certificates': certificates})
