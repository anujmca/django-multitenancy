"""multitenancy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from multitenancy.views import home, login, logout, index, public_createuser, public_create_certificate, \
    public_mycertificates

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('index', index, name='index'),
    path('public/createuser', public_createuser, name='public_createuser'),
    path('public/createcertificate', public_create_certificate, name='public_createcertificate'),
    path('public/mycertificates', public_mycertificates, name='public_mycertificates'),
]
