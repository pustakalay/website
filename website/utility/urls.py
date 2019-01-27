from django.conf.urls import url

from . import views

app_name = 'utility'
urlpatterns = [
    url('^$', views.index, name='index'),
]