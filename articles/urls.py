from django.urls import path
from . import views

app_name = "articles"
urlpatterns = [
    path('category/<str:category>/', views.article_by_category, name='by_cat'),
    path('all-articles/', views.AllArticleView.as_view(), name='all-articles'),
    path('new/', views.NewArticleView.as_view(), name='new-article'),
    path('search/<str:term>/', views.article_search)
    path('<slug:slug>/', views.ArticleDetailView.as_view(), name='article-detail')
    
]
