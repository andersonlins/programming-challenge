import os
import pathlib


import pandas as pd
from sqlalchemy import create_engine


class ReadFile:
    local = pathlib.Path(__file__).parent.parent

    @staticmethod
    def read_movie_file():
        tsv_movies = ReadFile.local.joinpath('files/title.basics.tsv.gz')
        tsv_rating = ReadFile.local.joinpath('files/title.ratings.tsv.gz')

        movies_df = pd.read_csv(tsv_movies, sep='\t', dtype='object', header=0)
        rating_df = pd.read_csv(tsv_rating, sep='\t', dtype='object', header=0)

        movies_rating_df = pd.merge(movies_df, rating_df, on='tconst')

        is_movie = movies_rating_df['titleType'] == 'movie'
        is_not_adult = movies_rating_df['isAdult'] == '0'
        is_higher_than_6 = movies_rating_df['averageRating'].astype(float) >= 6.0

        movies_rating_df = movies_rating_df[is_movie & is_not_adult & is_higher_than_6]

        movies_rating_df['startYear'] = movies_rating_df['startYear'].replace('\\N', int(0))
        movies_rating_df['endYear'] = movies_rating_df['endYear'].replace('\\N', int(0))
        movies_rating_df['runtimeMinutes'] = movies_rating_df['runtimeMinutes'].replace('\\N', int(0))

        return movies_rating_df

    @staticmethod
    def read_name_file():
        tsv_names = ReadFile.local.joinpath('files/name.basics.tsv.gz')

        names_df = pd.read_csv(tsv_names, sep='\t', dtype='object', header=0, nrows=1000)

        names_df.dropna()
        is_not_null = names_df['knownForTitles'] != '\\N'
        is_not_empty = names_df['knownForTitles'] != ''
        names_df['knownForTitles'] = names_df['knownForTitles'].replace('\\N', '')
        names_df['knownForTitles'] = names_df[is_not_null & is_not_empty]

        del names_df['primaryProfession']
        del names_df['nconst']

        names_df['birthYear'] = names_df['birthYear'].replace('\\N', int(0))
        names_df['deathYear'] = names_df['deathYear'].replace('\\N', int(0))

        return names_df

    @staticmethod
    def import_movies_data():
        movies_df = ReadFile.read_movie_file()

        name = os.environ['DB_NAME']
        user = os.environ['DB_USER']
        pwd = os.environ['DB_PASSWORD']
        host = os.environ['DB_HOST']
        port = os.environ['DB_PORT']
        connection_string = 'postgresql://{}:{}@{}:{}/{}'.format(user, pwd, host, port, name)
        engine = create_engine(connection_string)
        movies_df.to_sql('title', engine, if_exists='append', index=False)


    @staticmethod
    def import_names_data():
        names_df = ReadFile.read_name_file()

        name = os.environ['DB_NAME']
        user = os.environ['DB_USER']
        pwd = os.environ['DB_PASSWORD']
        host = os.environ['DB_HOST']
        port = os.environ['DB_PORT']
        connection_string = 'postgresql://{}:{}@{}:{}/{}'.format(user, pwd, host, port, name)
        engine = create_engine(connection_string)
        names_df.to_sql('person', engine, if_exists='append', index=False)
