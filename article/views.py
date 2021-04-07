from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from.models import Article
from django.contrib import messages
# Create your views here.

def articles(request):
    articles=Article.objects.all()

    return render(request,"articles.html",{"articles":articles})





def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")
@login_required(login_url="user:login")
def dashboard(request):
    articles=Article.objects.filter(author=request.user)
    return render(request,"dashboard.html",{"articles":articles})
@login_required(login_url="user:login")
def addarticle(request):

    form=ArticleForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        article=form.save(commit=False)
        article.author=request.user
        article.save()
        messages.success(request,"Makaleniz Başarıyla Eklenmiştir.")
        return redirect("article:dashboard")
    return render(request,"addarticle.html",{"form":form})

def detail(request,id):
    #article=Article.objects.filter(id=id).first()
    article=get_object_or_404(Article,id=id)
    return render(request,"detail.html",{"article":article})
@login_required(login_url="user:login")
def UpdateArticle(request,id):
    article=get_object_or_404(Article,id=id)
    form=ArticleForm(request.POST or None,request.FILES or None,instance=article)
    if form.is_valid():
        article=form.save(commit=False)
        article.author=request.user
        article.save()
        messages.success(request,"Makaleniz Başarıyla Güncellendi.")
        return redirect("index")

    return render(request,"update.html",{"form":form})
@login_required(login_url="user:login")
def DeleteArticle(request,id):
    article=get_object_or_404(Article,id=id)
    article.delete()
    messages.success(request,"Makale Başarıyla Silindi")

    return redirect("article:dashboard")
