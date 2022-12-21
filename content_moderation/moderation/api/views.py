from content_moderation.moderation.models import Movie
# from rest_framework import status
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
# from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .serializers import MovieSerializer



class MovieViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    lookup_field = "movie"
