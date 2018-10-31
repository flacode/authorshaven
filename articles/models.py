import datetime
from django.contrib.auth.models import User

from mongoengine import Document, EmbeddedDocument, EmbeddedDocumentField, StringField, DateTimeField, ReferenceField, CASCADE, ListField

class Comment(EmbeddedDocument):
    content = StringField()

class Article(Document):
    title = StringField(max_length=50, required=True)
    description = StringField(max_length=50, required=True)
    body = StringField(max_length=50, required=True)
    created_at = DateTimeField(default=datetime.datetime.now, required=True)
    updated_at = DateTimeField(null=True)
    comments = ListField(EmbeddedDocumentField(Comment))
    meta = {
        'index_background': True,
        'ordering': ['-created_at'],
        'indexes': [
            {
                'fields': ('title', 'created_at'),
                'partialFilterExpression' : { 'title': {'$lte': datetime.datetime.now()}}
            }
            ]
    }
    # author = ReferenceField(User, reverse_delete_rule=CASCADE)

    # def clean(self):
    #     """Used for validation and called by save"""
    #     print("This was called")
    #     pass

    def __str__(self):
        return self.title