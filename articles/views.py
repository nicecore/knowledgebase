from django.views.generic import TemplateView, CreateView, ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from django.urls import reverse

from .models import Article, Category

# Create your views here.


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
    

class AllArticleView(ListView):
    model = Article
    template_name = "all_articles.html"
    context_object_name = "all_articles"


def article_by_category(request, category):
    category = Category.objects.get(id=category)
    articles = Article.objects.filter(category=category)
    return render(
        request,
        "articles-by-category.html",
        {'articles': articles, 'category': category}
    )


class NewArticleView(CreateView):
    model = Article
    fields = ['title', 'content', 'category']
    template_name = 'new_article.html'
    
class ArticleDetailView(DetailView):
    model = Article
    queryset = Article.objects.all()
    
    
def article_search(request, term):
    