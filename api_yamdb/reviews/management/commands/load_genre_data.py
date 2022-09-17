from csv import DictReader

from django.core.management import BaseCommand
from reviews.models import Genre

ALREDY_LOADED_ERROR_MESSAGE = """
Если вам нужно перезагрузить данные из CSV-файла,
сначала удалите файл db.sqlite3, чтобы уничтожить базу данных.
Затем запустите 'python manage.py migrate' для новой пустой
базы данных с таблицами"""


class Command(BaseCommand):
    help = "Loads data from genre.csv"

    def handle(self, *args, **options):
        if Genre.objects.exists():
            print('Данные таблицы genre уже загружены!')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return

        print("Загружаем данные в таблицу genre")
        with open('./static/data/genre.csv', encoding='utf-8') as file:
            data = DictReader(file)
            for row in data:
                genre = Genre(
                    id=row['id'],
                    name=row['name'],
                    slug=row['slug'],
                )
                genre.save()
        print("Данные в таблицу genre загружены")
