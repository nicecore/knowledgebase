from django.urls import path
from . import views

app_name = "articles"
urlpatterns = [
    path('all-articles/', views.AllArticleView.as_view()),
    # path('new/', views.NewArticleView.as_view()),
    path('articles/<category>/', views.article_by_category, name='by_cat')
]
