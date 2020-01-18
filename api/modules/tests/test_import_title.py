from rest_framework.test import APITestCase

from modules.parser_tsv_import import import_data_files


class TitleTest(APITestCase):
    def import_title_by_file(self):
        from django.apps import apps
        try:
            import_data_files(apps)
        except:
            print("error")
        self.assertEqual(True, False)
