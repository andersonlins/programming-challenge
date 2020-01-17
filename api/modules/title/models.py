from django.db import models


class Title(models.Model):
    tconst = models.CharField(
        db_column='tconst',
        max_length=300,
        primary_key=True,
        null=False,
        blank=False,
        unique=True
    )

    titleType = models.CharField(
        db_column='titleType',
        max_length=300,
        null=False,
        blank=False
    )

    primaryTitle = models.CharField(
        db_column='primaryTitle',
        max_length=300,
        null=False,
        blank=False
    )

    originalTitle = models.CharField(
        db_column='originalTitle',
        max_length=300,
        null=False,
        blank=False
    )

    isAdult = models.BooleanField(
        db_column='isAdult',
        null=False,
        default=False,
        blank=False
    )

    startYear = models.IntegerField(
        db_column='startYear'
    )

    endYear = models.IntegerField(
        db_column='endYear'
    )

    runtimeMinutes = models.IntegerField(
        db_column='runtimeMinutes',
    )

    genres = models.CharField(
        db_column='genres',
        max_length=300,
        null=False,
        blank=False
    )

    averageRating = models.FloatField(
        db_column='averageRating',
        null=False
    )

    numVotes = models.IntegerField(
        db_column='numVotes',
        null=False
    )

    def __str__(self):
        return str(self.originalTitle)

    class Meta:
        managed = True
        db_table = 'title'
        default_permissions = ()


class Person(models.Model):
    id = models.BigAutoField(
        db_column='id',
        primary_key=True,
        null=False
    )

    primaryName = models.CharField(
        db_column='primaryName',
        max_length=120,
        null=False,
        blank=False
    )

    birthYear = models.IntegerField(
        db_column='birthYear',
        default=None,
        null=True
    )

    deathYear = models.IntegerField(
        db_column='deathYear',
        default=None,
        null=True
    )

    knownForTitles = models.CharField(
        db_column='knownForTitles',
        max_length=300,
        null=True,
        blank=True
    )

    def __str__(self):
        return str(self.primaryName)

    class Meta:
        managed = True
        db_table = 'person'
        default_permissions = ()
