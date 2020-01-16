import csv
import os

from django.db import transaction, DatabaseError

from modules.manager_inserts import BulkCreateManager


def import_data_files(apps):
    import_titles(apps)
    import_ratings(apps)
    import_names(apps)


def import_titles(apps):
    file = os.path.join(os.path.dirname(__file__), 'tests/files/title.basics.tsv')

    with open(file, 'r') as tsvfile:
        # bulk_mgr = BulkCreateManager(chunk_size=25000)
        reader = csv.reader(tsvfile, delimiter='\t')
        next(reader)

        data_list = list(reader)

        for row in data_list[:1000]:
            try:
                title = create_title(row, apps)
                # bulk_mgr.add(title)
            except:
                print("error")


def import_ratings(apps):
    file = os.path.join(os.path.dirname(__file__), 'tests/files/title.ratings.tsv')

    with open(file, 'r') as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        next(reader)
        data_list = list(reader)
        for row in data_list[:1000]:
            create_rating(row, apps)


def import_names(apps):
    file = os.path.join(os.path.dirname(__file__), 'tests/files/name.basics.tsv')

    with open(file, 'r') as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        next(reader)
        data_list = list(reader)
        for row in data_list[:1000]:
            create_person(row, apps)


def create_title(data, apps):
    title_model = apps.get_model('title', 'Title')

    try:
        title = title_model.objects.get(tconst=data[0])
    except title_model.DoesNotExist:
        if data is not None and len(data) > 0:
            title = title_model()
            title.tconst = data[0]
            title.type = create_type(data[1], apps)
            title.primary_title = data[2]
            title.original_title = data[3]
            title.is_adult = data[4]
            title.start_year = int(data[5]) if is_number(data[5]) else None
            title.end_year = int(data[6]) if is_number(data[6]) else None
            title.runtime_minutes = int(data[7]) if is_number(data[7]) else None
            if is_valid_index(8, data):
                genres = create_genres(data[8], apps)
                if len(genres) > 0:
                    title.genres.add(*genres)
            title.save()
            return title


def create_rating(data, apps):
    rating_model = apps.get_model('title', 'Rating')

    try:
        rating = rating_model.objects.get(tconst=data[0])
    except rating_model.DoesNotExist:
        if data is not None and len(data) > 0:
            rating = rating_model()
            title = get_title(data[0], apps)
            if title is not None:
                rating.tconst = title
                rating.average_rating = float(data[1])
                rating.num_votes = int(data[2])
                rating.save()


def create_person(data, apps):
    person_model = apps.get_model('title', 'Person')

    try:
        person = person_model.objects.get(nconst=data[0])
    except person_model.DoesNotExist:
        if data is not None and len(data) > 0:
            person = person_model()
            person.nconst = data[0]
            person.primary_name = data[1]
            person.birth_year = int(data[2]) if is_number(data[2]) else None
            person.death_year = int(data[3]) if is_number(data[3]) else None
            person.save()

            if is_valid_index(4, data):
                professions = create_professions(data[4], apps)
                if len(professions) > 0:
                    person.professions.add(*professions)

            if is_valid_index(5, data):
                titles = get_titles(data[5], apps)
                if len(titles) > 0:
                    person.know_for_titles.add(*titles)

            try:
                person.save()
            except:
                print("aaaa")

def get_title(id_title, apps):
    title_model = apps.get_model('title', 'Title')

    try:
        return title_model.objects.get(tconst=id_title)
    except:
        return None


def create_type(name, apps):
    type_model = apps.get_model('title', 'Type')
    return type_model.objects.get_or_create(name=name)[0]


def create_genres(genres_data, apps):
    genre_model = apps.get_model('title', 'Genre')

    genres = []

    if genres_data is None or (genres_data is not None and (r"\N".lower() == genres_data.lower() or len(genres_data) == 0)) :
        return genres

    genres_strings = genres_data.split(',')

    for item in genres_strings:
        genre = genre_model.objects.get_or_create(name=item)[0]
        genres.append(genre)

    return genres


def create_professions(profession_data, apps):
    profession_model = apps.get_model('title', 'Profession')

    professions = []

    if not profession_data or r"\N" == profession_data:
        return professions

    profession_strings = profession_data.split(',')

    for item in profession_strings:
        profession = profession_model.objects.get_or_create(name=item)[0]
        profession.save()
        professions.append(profession)

    return professions


def get_titles(title_data, apps):
    title_model = apps.get_model('title', 'Title')

    titles = []

    if not title_data or r"\N" == title_data:
        return titles

    title_strings = title_data.split(',')

    for item in title_strings:
        try:
            title = title_model.objects.get(tconst=item)
            titles.append(title)
        except:
            continue

    return titles


def is_number(variable):
    try:
        int(variable)
        return True
    except:
        return False


def is_valid_index(index, data):
    return 0 <= index < len(data)