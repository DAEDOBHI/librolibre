from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import *
# Create your views here.
Posts = Post.objects.all()
def post(request):
    return render(request,'post/index.html',context ={"books":Posts})
def authors(request):
    Authors = Author.objects.all()
    context = {
        "authors": Authors
    }
    return render(request, 'post/authors.html',context = context)

def book(request,id):
    try:
        post = Post.objects.get(pk=id)
    except Exception:
        #return HttpResponseNotFound("Ese libro no exite")
        return render(request,'demo/404.html', status = 404)

    context = {
        "post": post,
    }
    return render(request,'post/post.html',context = context )

def author(request,id):
    try:
        author = Author.objects.get(pk=id)
        
    except Exception:
        #return HttpResponseNotFound("Ese libro no exite")
        return render(request,'demo/404.html', status = 404)
    
    context = {
            "authors": author
        }
    
    return render(request, 'post/author.html',context = context)

def author_detail(request,id):

    author = Author.objects.get(pk=id)
    posts = author.books.all()
    context = {
        'author' : author,
        'books' : Posts,
    }
    return render(
        request,
        'post/author_detail.html',
        context = context
    )

def country_detail(request,id):

    country = Country.objects.get(pk=id)
    authors = country.authors.all()
    context = {
        'country' : country,
        'authors' : authors,
    }
    return render(
        request,
        'post/country_detail.html',
        context = context
    )