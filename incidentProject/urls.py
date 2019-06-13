"""incidentProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth.decorators import login_required
from django.urls import path, re_path, include

from authOrion.views import StartView, RegisterFormView, LoginFormView, LogoutView
from adminIncident.views import AdminIncidentView

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^adminincident/', include('adminIncident.urls')),
    re_path(r'^orion/', include('orion.urls')),
    re_path(r'^$', login_required(StartView.as_view()), name="start"),

    #Auth
    re_path(r'^register/', RegisterFormView.as_view(), name="register"),
    re_path(r'^login/', LoginFormView.as_view(), name="login"),
    re_path(r'^logout/', LogoutView.as_view(), name="logout"),
    re_path(r'^changepassword/', LogoutView.as_view(), name="changepassword"),
]
