# Generated by Django 2.2.4 on 2020-01-17 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False)),
                ('primaryName', models.CharField(db_column='primaryName', max_length=120)),
                ('birthYear', models.IntegerField(db_column='birthYear', default=None, null=True)),
                ('deathYear', models.IntegerField(db_column='deathYear', default=None, null=True)),
                ('knownForTitles', models.CharField(blank=True, db_column='knownForTitles', max_length=300, null=True)),
            ],
            options={
                'db_table': 'person',
                'managed': True,
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('tconst', models.CharField(db_column='tconst', max_length=300, primary_key=True, serialize=False, unique=True)),
                ('titleType', models.CharField(db_column='titleType', max_length=300)),
                ('primaryTitle', models.CharField(db_column='primaryTitle', max_length=300)),
                ('originalTitle', models.CharField(db_column='originalTitle', max_length=300)),
                ('isAdult', models.BooleanField(db_column='isAdult', default=False)),
                ('startYear', models.IntegerField(db_column='startYear')),
                ('endYear', models.IntegerField(db_column='endYear')),
                ('runtimeMinutes', models.IntegerField(db_column='runtimeMinutes')),
                ('genres', models.CharField(db_column='genres', max_length=300)),
                ('averageRating', models.FloatField(db_column='averageRating')),
                ('numVotes', models.IntegerField(db_column='numVotes')),
            ],
            options={
                'db_table': 'title',
                'managed': True,
                'default_permissions': (),
            },
        ),
    ]
