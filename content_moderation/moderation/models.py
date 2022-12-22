from django.db import models
from django_quill.fields import QuillField
from autoslug import AutoSlugField

# Create your models here.
class Movie(models.Model):
    title = models.CharField("Movie title", max_length=150)
    slug = AutoSlugField(populate_from='title') # auto field
    poster = models.URLField("Movie Poster", help_text="use a url like: https://www.criticsinc.com/photos/movieposters/l/lightyear.jpg")
    summary = QuillField("Movie Summary")
    violence = QuillField("Violence & Gore")
    violence_rating = models.IntegerField("Violence & Gore Percentage", help_text="percentage out of 100 where 100 is the maximum")
    language = QuillField("Language")
    language_rating = models.IntegerField("Language Percentage", help_text="percentage out of 100 where 100 is the maximum")
    inappropriate = QuillField("Inappropriate")
    inappropriate_rating = models.IntegerField("Inappropriate Percentage", help_text="percentage out of 100 where 100 is the maximum")
    drug_usage = QuillField("Drug Usage")
    religious_imagery = QuillField("Religious Imagery")
    year = models.IntegerField("Year of Publish")
    rating = models.CharField(help_text="movie rating (eg, PG, R Rated)", max_length=20)
    duration = models.CharField("Movie Duration", help_text="eg 2h 33m", max_length=10)

    def __str__(self):
        return self.title