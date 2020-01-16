import unittest

from modules.parser_tsv_import import create_genres


class ImportFiles(unittest.TestCase):
    def test_create_genres_when_data_is_encoded(self):
        from django.apps import apps
        data_genre = r"\N"

        genres = create_genres(data_genre, apps)

        self.assertEqual(len(genres), 0, "Should be return an empty array")

    def test_create_genres_when_data_is_empty(self):
        from django.apps import apps
        data_genre = ""

        genres = create_genres(data_genre, apps)

        self.assertEqual(len(genres), 0, "Should be return an empty array")


if __name__ == '__main__':
    unittest.main()
