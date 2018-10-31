from django.urls import path
from articles import views

urlpatterns = [
    path('articles/', views.ArticleView.as_view()),
    path('articles/<str:id>/', views.ArticleViewUpdateDelete.as_view()),
]