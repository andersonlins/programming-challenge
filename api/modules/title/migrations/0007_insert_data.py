from django.db import migrations

from modules.parser_tsv_import import import_data_files


def insert_data(apps, schema_editor):
    import_data_files(apps)


class Migration(migrations.Migration):

    dependencies = [
        ('title', '0006_update_default_values'),
    ]

    operations = [
        migrations.RunPython(insert_data),
    ]
