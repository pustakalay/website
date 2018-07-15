from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Book
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    bookList = Book.objects.all().order_by('-rank')
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
    filter = request.GET.get('f')

    if filter == 'Title':
        bookList = searchTitle(query)
    elif filter == 'Author':
        bookList = searchAuthor(query)
    elif filter == 'Isbn10/13':
        bookList = searchIsbn(query)
    elif filter == 'Publisher':
        bookList = searchPublisher(query)
    elif filter == 'None':
        bookListTitle = searchTitle(query)
        bookListAuthor = searchAuthor(query)
        bookListIsbn = searchIsbn(query)
        bookListPublisher = searchPublisher(query)
        bookList = bookListTitle | bookListAuthor | bookListIsbn | bookListPublisher

    orderBookList = bookList.order_by('-rank')
    context = {'bookList': orderBookList}
    return render(request, 'bookapp/index.html', context)

def searchTitle(query):
    bookList = Book.objects.all().filter(Q(title__icontains=query))
    return bookList

def searchAuthor(query):
    bookList = Book.objects.all().filter(Q(author__icontains=query))
    return bookList

def searchIsbn(query):
    bookList = Book.objects.all().filter(Q(isbn10__iexact=query) | Q(isbn13__iexact=query))
    return bookList

def searchPublisher(query):
    bookList = Book.objects.all().filter(Q(publisher__icontains=query))
    return bookList