from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Book
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

from django.http import HttpResponse


def index(request):
    bookList = Book.objects.all().order_by('-numberOfCopiesSold')
    context = {'bookList': bookList}
    return render(request, 'bookapp/index.html', context)

def bookDetail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'bookapp/bookdetails.html', {'book': book})

def buyBook(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.numberOfCopiesSold  += 1
    book.save()
    return HttpResponseRedirect(reverse('bookapp:index'))

def search(request):
    query = request.GET.get('q')
    bookList = Book.objects.all().filter(Q(title__icontains=query) | Q(author__icontains=query) | Q(publisher__icontains=query) | Q(isbn__iexact=query))
    bookList.order_by('-numberOfCopiesSold')
    context = {'bookList': bookList}
    return render(request, 'bookapp/index.html', context)

