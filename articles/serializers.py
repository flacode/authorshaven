import datetime
from rest_framework import serializers
from articles.models import Article, Comment
from django.contrib.auth.models import User
from rest_framework_mongoengine import serializers as mongoserializer


class CommentSerializer(mongoserializer.EmbeddedDocumentSerializer):
    class Meta:
        model = Comment
        fields = ('content',)


class ArticleSerializer(mongoserializer.DocumentSerializer):
    comments = CommentSerializer(many=True)
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('updated_at', 'created_at')

    def create(self, validated_data):
        comments_data = validated_data.pop('comments')
        article = Article.objects.create(**validated_data)
        for comment in comments_data:
            article.comments.append(Comment(**comment))
        article.save()
        return article

    def update(self, instance, validated_data):
        comments_data = validated_data.pop('comments')
        updated_instance = super(ArticleSerializer, self).update(instance, validated_data)
        updated_instance.updated_at = datetime.datetime.now()
        for comment in comments_data:
            updated_instance.comments.append(Comment(**comment))
        updated_instance.save()
        return updated_instance