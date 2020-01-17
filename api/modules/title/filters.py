from django.db.models import QuerySet, Q
from django_filters.rest_framework import filterset, filters

from commons import choices
from modules.title import models


class TitleFilter(filterset.FilterSet):
    titleType = filters.CharFilter(lookup_expr=choices.FILTER_EQUALS, field_name='titleType')
    primaryTitle = filters.CharFilter(lookup_expr=choices.FILTER_LIKE)
    originalTitle = filters.CharFilter(lookup_expr=choices.FILTER_LIKE)
    isAdult = filters.BooleanFilter()
    startYear = filters.NumberFilter()
    endYear = filters.NumberFilter()
    runtimeMinutes = filters.NumberFilter()
    genres = filters.CharFilter(lookup_expr=choices.FILTER_LIKE, field_name='genres')
    averageRating = filters.NumberFilter()

    class Meta:
        model = models.Title
        fields = ['titleType', 'primaryTitle', 'originalTitle', 'isAdult', 'startYear', 'endYear', 'runtimeMinutes', 'genres', 'averageRating']


class PersonFilter(filterset.FilterSet):
    primaryTitle = filters.CharFilter(lookup_expr=choices.FILTER_LIKE)
    birthYear = filters.NumberFilter()
    deathYear = filters.NumberFilter()

    class Meta:
        model = models.Person
        fields = ['primaryTitle', 'birthYear', 'deathYear']