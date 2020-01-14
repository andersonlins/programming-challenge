import django
from django.db import models


class MovieType(models.Model):
    id = models.BigAutoField(
        db_column='id',
        primary_key=True,
        null=False
    )

    name = models.CharField(
        db_column='name',
        max_length=100,
        null=False,
        blank=False,
        unique=True
    )

    def __str__(self):
        return str(self.name)

    class Meta:
        managed = True
        db_table = 'movie_type'
        default_permissions = ()


class Genre(models.Model):
    id = models.BigAutoField(
        db_column='id',
        primary_key=True,
        null=False,
    )

    name = models.CharField(
        db_column='name',
        max_length=120,
        null=False,
        blank=False,
        unique=True
    )

    def __str__(self):
        return str(self.name)

    class Meta:
        managed = True
        db_table = 'genre'
        default_permissions = ()


class Movie(models.Model):
    tconst = models.CharField(
        db_column='tconst',
        max_length=300,
        primary_key=True,
        null=False,
        blank=False,
        unique=True
    )

    type = models.ForeignKey(MovieType,
                             db_column='id_movie_type',
                             on_delete=django.db.models.deletion.DO_NOTHING,
                             related_name="movie",
                             null=False,
                             db_index=False)

    primary_title = models.CharField(
        db_column='primary_title',
        max_length=300,
        null=False,
        blank=False
    )

    original_title = models.CharField(
        db_column='original_title',
        max_length=300,
        null=False,
        blank=False
    )

    is_adult = models.BooleanField(
        db_column='is_adult',
        null=False,
        default=False,
        blank=False
    )

    start_year = models.IntegerField(
        db_column='start_year',
        null=False
    )

    end_year = models.IntegerField(
        db_column='end_year',
        null=True
    )

    runtime_minutes = models.IntegerField(
        db_column='runtime_minutes',
        null=False
    )

    genres = models.ManyToManyField(Genre,
                                    blank=False,
                                    related_name='movies')

    def __str__(self):
        return str(self.original_title)

    class Meta:
        managed = True
        db_table = 'movie'
        default_permissions = ()


class Rating(models.Model):
    average_rating = models.FloatField(
        db_column='average_rating',
        null=False
    )

    num_votes = models.IntegerField(
        db_column='num_votes',
        null=False
    )

    tconst = models.ForeignKey(Movie,
                               db_column='tconst',
                               on_delete=django.db.models.deletion.DO_NOTHING,
                               related_name="rating",
                               null=False,
                               db_index=False)

    def __str__(self):
        return str(self.average_rating)

    class Meta:
        managed = True
        db_table = 'rating'
        default_permissions = ()


class Profession(models.Model):
    id = models.BigAutoField(
        db_column='id',
        primary_key=True,
        null=False
    )

    name = models.CharField(
        db_column='name',
        max_length=120,
        null=False,
        blank=False,
        unique=True
    )

    def __str__(self):
        return str(self.name)

    class Meta:
        managed = True
        db_table = 'profession'
        default_permissions = ()


class Person(models.Model):
    nconst = models.CharField(
        db_column='nconst',
        max_length=300,
        primary_key=True,
        null=False,
        blank=False,
        unique=True
    )

    primary_name = models.CharField(
        db_column='primary_name',
        max_length=120,
        null=False,
        blank=False
    )

    birth_year = models.IntegerField(
        db_column='birth_year',
        null=False
    )

    death_year = models.IntegerField(
        db_column='death_year',
        null=True
    )

    professions = models.ManyToManyField(Profession,
                                         blank=False,
                                         related_name='persons_professions')

    know_for_titles = models.ManyToManyField(Movie,
                                             blank=False,
                                             related_name='persons_movies')

    def __str__(self):
        return str(self.primary_name)

    class Meta:
        managed = True
        db_table = 'person'
        default_permissions = ()
