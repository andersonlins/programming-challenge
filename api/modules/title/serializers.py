from rest_framework import serializers

from modules.title import models


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Type
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        fields = '__all__'


class TitleSerializer(serializers.ModelSerializer):
    type_obj = TypeSerializer(source='type', read_only=True)
    genres_obj = GenreSerializer(source='genres', read_only=True, many=True)

    class Meta:
        model = models.Title
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rating
        fields = '__all__'


class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profession
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    professions_obj = ProfessionSerializer(source='profession', read_only=True, many=True)
    titles_obj = TitleSerializer(source='know_for_titles', read_only=True, many=True)

    class Meta:
        model = models.Person
        fields = '__all__'
