from content_moderation.moderation.models import Movie
from rest_framework import serializers
from django_quill.drf.fields import QuillHtmlField

class MovieSerializer(serializers.ModelSerializer):
    # https://github.com/LeeHanYeong/django-quill-editor/issues/81#issuecomment-1111327959
    summary = QuillHtmlField()
    violence = QuillHtmlField()
    language = QuillHtmlField()
    inappropriate = QuillHtmlField()
    drug_usage = QuillHtmlField()
    religious_imagery = QuillHtmlField()

    class Meta:
        model = Movie
        fields = [
            'title',
            'poster',
            'summary',
            'violence',
            'violence_rating',
            'language',
            'language_rating',
            'inappropriate',
            'inappropriate_rating',
            'drug_usage',
            'religious_imagery',
            'duration',
            'slug',
            'year',
            'rating',
        ]
