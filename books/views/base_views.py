from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from ..models import Books
from django.db.models import Q, Count

def index(request):

    books_list = Books.objects.order_by('-register_date')
    context = {'books_list':books_list}
    return render(request, 'books/books_list.html', context)


def detail(request, books_id):
    """
    pybo 내용 출력
    """
    books = get_object_or_404(Books, pk=books_id)
    context = {'books': books}
    return render(request, 'books/books_detail.html', context)
