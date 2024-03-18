from django.apps import AppConfig



class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    '''def ready(self):
            super().ready()
            from . import csv_to_database
            csv_to_database.load_data_from_csv()'''