from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from books.models import Book, Categorie, Author, Publishers, BookRequest
from extra.models import Comment, LikeBook, LikeComment, BookMarck
from django.contrib import messages
from django.db.models import Count
from books.forms import NewBook
from accounts.models import CustomUserModel


def books(request):
    context = {
        'books': Book.objects.all(),
        'cate': Categorie.objects.all(),
    }
    return render(request, 'index.html', context)


def category(request, cats):
    context = {
        'separation': get_list_or_404(Book, category= cats),
        'cate': Categorie.objects.all(),
    }
    return render(request, 'index.html', context)


def search_author(request, auth):
    context = {
        'separation': get_list_or_404(Book, author= auth),
        'cate': Categorie.objects.all(),
    }
    return render(request, 'index.html', context)



def detail_book(request, pk):
    book = Book.objects.get(id=pk)
    content = {
        'detail' : book,
        'comment': Comment.objects.filter(book=pk),
        'like' : LikeBook.objects.filter(book=book, vote='L').count(),
        'dislike' : LikeBook.objects.filter(book=book, vote='D').count(),
    }
    return render(request, 'books/detail.html', content)    


        
@login_required(login_url='login')       
def new_book(request):
    if request.method == 'POST':
        book_form = NewBook(request.POST)
        if book_form.is_valid():
            book_form.save(commit=False)
            customuser = CustomUserModel.objects.get(user=request.user)
            book_form.user = customuser
            book_form.save()
            book_form.save_m2m()
            messages.success(request, 'Your registration was successfully done.')
            return redirect('home')
        else:
            print('this is a test in case of failure.')
    book_form = NewBook()
    content = {
        'new_book':book_form,
    }
    return render(request, 'index2.html', content)


@login_required(login_url='login')
def new_author(request):
    if request.method == 'POST':
        pass
        
    

def request_book(request):
    if request.method == 'POST':
        pass