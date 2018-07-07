from django.conf.urls import url

from . import views

app_name = 'bookapp'
urlpatterns = [
    url(r'', views.index, name='index'),
    url(r'book/<int:book_id>/', views.bookDetail, name='bookDetail'),
    url(r'buy/<int:book_id>/', views.buyBook, name='buyBook'),
    url(r'search/', views.search, name='search'),
]