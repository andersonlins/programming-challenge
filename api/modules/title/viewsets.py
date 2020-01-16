from rest_framework import viewsets

from modules.title import models, serializers, filters


class TypeViewSet(viewsets.ModelViewSet):
    queryset = models.Type.objects.all()
    serializer_class = serializers.TypeSerializer
    filter_class = filters.TypeFilter
    ordering = ('name',)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer
    filter_class = filters.GenreFilter
    ordering = ('name',)


class ProfessionViewSet(viewsets.ModelViewSet):
    queryset = models.Profession.objects.all()
    serializer_class = serializers.ProfessionSerializer
    filter_class = filters.ProfessionFilter
    ordering = ('name',)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = models.Rating.objects.all()
    serializer_class = serializers.RatingSerializer
    filter_class = filters.RatingFilter
    ordering = ('name',)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = models.Title.objects.prefetch_related('types').all()
    serializer_class = serializers.TitleSerializer
    filter_class = filters.TitleFilter
    ordering = ('primary_title',)

    def list(self, request, *args, **kwargs):
        title_type = models.Type.objects.filter(name__exact='movie')
        self.queryset = models.Title.objects.filter(type__id=title_type.id)
        self.serializer_class = serializers.TitleSerializer
        return super(TitleViewSet, self).list(request, *args, **kwargs)


class PersonViewSet(viewsets.ModelViewSet):
    queryset = models.Person.objects.prefetch_related('professions').all()
    serializer_class = serializers.PersonSerializer
    filter_class = filters.PersonFilter
    ordering = ('primary_name',)

    def list(self, request, *args, **kwargs):
        self.queryset = models.Person.objects.all()
        self.serializer_class = serializers.PersonSerializer
        return super(PersonViewSet, self).list(request, *args, **kwargs)
