from django.db import models
from django_quill.fields import QuillField
from autoslug import AutoSlugField

# Create your models here.
class Movie(models.Model):
    title = models.CharField("Movie title", max_length=150)
    slug = AutoSlugField(populate_from='title') # auto field
    poster = models.URLField("Movie Poster")
    summary = QuillField()
    violence = QuillField()
    violence_rating = models.IntegerField()
    language = QuillField()
    language_rating = models.IntegerField()
    inappropriate = QuillField()
    inappropriate_rating = models.IntegerField()
    drug_usage = QuillField()
    religious_imagery = QuillField()
    year = models.IntegerField()
    rating = models.CharField(help_text="movie rating (eg, PG, R Rated)", max_length=20)
    duration = models.CharField(help_text="eg 2h 33m", max_length=10)

    def __str__(self):
        return self.title