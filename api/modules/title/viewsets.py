from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from modules.title import models, serializers, filters
from modules.title.serializers import TitleSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 1


class TitleViewSet(viewsets.ModelViewSet):
    queryset = models.Title.objects.all()
    serializer_class = serializers.TitleSerializer
    filter_class = filters.TitleFilter
    ordering = ('primaryTitle',)

    def list(self, request, *args, **kwargs):
        self.queryset = models.Title.objects.filter(titleType='movie')
        self.serializer_class = serializers.TitleSerializer

        return super(TitleViewSet, self).list(request, *args, **kwargs)

    @action(detail=False, methods=['GET'])
    def get_by_year(self, request):
        year = request.query_params['year']
        genre = request.query_params.get('genre')

        query = None

        if year is not None and (year and int(year) > 0):
            query = models.Title.objects.filter(Q(titleType='movie')
                                                & (Q(startYear__exact=year) | Q(endYear__exact=year)))

        if genre is not None and query is not None:
            query = query.filter(titleType__contains=genre)

        return Response(serializers.TitleSerializer(query.order_by('-averageRating')[0:10], many=True).data, status=status.HTTP_200_OK)


class PersonViewSet(viewsets.ModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer
    filter_class = filters.PersonFilter
    ordering = ('primaryName',)

    def list(self, request, *args, **kwargs):
        self.queryset = models.Person.objects.all()
        self.serializer_class = serializers.PersonSerializer
        return super(PersonViewSet, self).list(request, *args, **kwargs)
