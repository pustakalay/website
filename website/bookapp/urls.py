from django.conf.urls import url

from . import views

app_name = 'bookapp'
urlpatterns = [
    url('^$', views.index, name='index'),
    url(r'^(?P<book_id>[0-9000]+)/book/$', views.bookDetail, name='bookDetail'),
    url(r'^(?P<book_id>[0-9000]+)/buy/$', views.buyBook, name='buyBook'),
    url(r'search/', views.search, name='search'),
]