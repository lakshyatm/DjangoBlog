from django.shortcuts import render,redirect, get_object_or_404
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return HttpResponse("<html><body>    <h1>Article List</<h1>
    <div class="articles">
      {% for article in articles %}
        <div class="article">
          <h2><a href="{% url 'articles:detail' slug=article.slug %}">{{article.title}}</a></h2>
          <p>{{article.snippet}}</p>
          <p>{{article.date}}</p>
          <p class="author">added by {{article.author.username}}</p>

        </div>
      {% endfor %}
    </div></body></html>")

def article_detail(request,slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'article_detail.html',{'article':article})

@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request,'article_create.html',{'form':form})

def LikeView(request):
    post = get_object_or_404(User, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article_detail',args=[str(pk)]))
