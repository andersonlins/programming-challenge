import os
from os import path

import pandas as pd
from sqlalchemy import create_engine


class ReadFile:
    # local = path.abspath(path.join(__file__, "../../../dataset"))
    local = os.path.dirname(__file__) + '/tests/files/'

    @staticmethod
    def read_movie_file():
        tsv_movies = ReadFile.local + 'title.basics.tsv'
        tsv_rating = ReadFile.local + 'title.ratings.tsv'

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
        tsv_names = ReadFile.local + 'name.basics.tsv'

        names_df = pd.read_csv(tsv_names, sep='\t', dtype='object', header=0)

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
        engine = create_engine('postgresql://postgres:123456@localhost:5432/titles_db')
        movies_df.to_sql('title', engine, if_exists='append', index=False)


    @staticmethod
    def import_names_data():
        names_df = ReadFile.read_name_file()
        engine = create_engine('postgresql://postgres:123456@localhost:5432/titles_db')
        names_df.to_sql('person', engine, if_exists='append', index=False)
