from rest_framework import serializers

from modules.title import models


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Title
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = '__all__'
