"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url('^$', views.home_page, name = 'home'),
    url('^logout/$', auth_views.LogoutView.as_view(), name = 'logout'),
    url('^login/$', views.login_page, name = 'login_page'),
    url(r'^auth/', include('social_django.urls', namespace='social')), 
    url('^gotobooks/$', views.gotobooks, name = 'gotobooks'),
    url('^register/$', views.register_page, name = 'register_page'),
    url('admin/', admin.site.urls),
    url('utility/', include('utility.urls')),
    url('books/', include('bookapp.urls')),
]
