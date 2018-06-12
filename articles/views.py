from django.views.generic import TemplateView, CreateView
from django.views.generic.detail import DetailView
from django.shortcuts import render

from .models import Article, Category

# Create your views here.


class HomeView(TemplateView):
    template_name = "home.html"
    

class NewArticleView(CreateView):
    pass
class ArticleDetailView(DetailView):
    model = Article
