import django
from django.db import models


class Type(models.Model):
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
        db_table = 'title_type'
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


class Title(models.Model):
    tconst = models.CharField(
        db_column='tconst',
        max_length=300,
        primary_key=True,
        null=False,
        blank=False,
        unique=True
    )

    type = models.ForeignKey(Type,
                             db_column='id_title_type',
                             on_delete=django.db.models.deletion.DO_NOTHING,
                             related_name="title",
                             null=True,
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
        default=None,
        null=True
    )

    end_year = models.IntegerField(
        db_column='end_year',
        default=None,
        null=True
    )

    runtime_minutes = models.IntegerField(
        db_column='runtime_minutes',
        default=None,
        null=True
    )

    genres = models.ManyToManyField(Genre, related_name='titles')

    def __str__(self):
        return str(self.original_title)

    class Meta:
        managed = True
        db_table = 'title'
        default_permissions = ()


class Rating(models.Model):
    tconst = models.OneToOneField(Title,
                                  db_column='tconst',
                                  on_delete=django.db.models.deletion.DO_NOTHING,
                                  related_name="rating",
                                  null=False,
                                  primary_key=True)

    average_rating = models.FloatField(
        db_column='average_rating',
        null=False
    )

    num_votes = models.IntegerField(
        db_column='num_votes',
        null=False
    )

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
        default=None,
        null=True
    )

    death_year = models.IntegerField(
        db_column='death_year',
        default=None,
        null=True
    )

    professions = models.ManyToManyField(Profession, related_name='persons_professions')

    know_for_titles = models.ManyToManyField(Title, related_name='persons_titles')

    def __str__(self):
        return str(self.primary_name)

    class Meta:
        managed = True
        db_table = 'person'
        default_permissions = ()
