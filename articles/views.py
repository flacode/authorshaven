from django.shortcuts import render
from articles.models import Article
from articles.serializers import ArticleSerializer
from rest_framework import generics
from rest_framework.response import Response
import datetime


class ArticleView(generics.ListCreateAPIView):

    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.objects


class ArticleViewUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = ArticleSerializer
    
    def get_queryset(self):
        return Article.objects
        