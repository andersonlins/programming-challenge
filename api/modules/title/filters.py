from django_filters.rest_framework import filterset, filters

from commons import choices
from modules.title import models


class TypeFilter(filterset.FilterSet):
    name = filters.CharFilter(lookup_expr=choices.FILTER_LIKE)

    class Meta:
        model = models.Type
        fields = ['name']


class GenreFilter(filterset.FilterSet):
    name = filters.CharFilter(lookup_expr=choices.FILTER_LIKE)

    class Meta:
        model = models.Genre
        fields = ['name']


class TitleFilter(filterset.FilterSet):
    type_name = filters.CharFilter(lookup_expr=choices.FILTER_EQUALS, field_name='types__name')
    primary_title = filters.CharFilter(lookup_expr=choices.FILTER_LIKE)
    original_title = filters.CharFilter(lookup_expr=choices.FILTER_LIKE)
    is_adult = filters.BooleanFilter()
    start_year = filters.NumberFilter()
    end_year = filters.NumberFilter()
    runtime_minutes = filters.NumberFilter()

    class Meta:
        model = models.Title
        fields = ['type_name', 'primary_title', 'original_title', 'is_adult', 'start_year', 'end_year', 'runtime_minutes']


class RatingFilter(filterset.FilterSet):
    average_rating = filters.NumberFilter()
    num_votes = filters.NumberFilter()
    tconst = filters.NumberFilter(field_name='tconst__tconst')

    class Meta:
        model = models.Rating
        fields = ['average_rating', 'num_votes', 'tconst']


class ProfessionFilter(filterset.FilterSet):
    name = filters.CharFilter(lookup_expr=choices.FILTER_LIKE)

    class Meta:
        model = models.Profession
        fields = ['name']


class PersonFilter(filterset.FilterSet):
    primary_title = filters.CharFilter(lookup_expr=choices.FILTER_LIKE)
    birth_year = filters.NumberFilter()
    death_year = filters.NumberFilter()

    class Meta:
        model = models.Rating
        fields = ['primary_title', 'birth_year', 'death_year']