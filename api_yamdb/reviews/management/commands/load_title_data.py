from csv import DictReader
from django.core.management import BaseCommand
from django.shortcuts import get_object_or_404

from reviews.models import Title, Category


ALREDY_LOADED_ERROR_MESSAGE = """
Если вам нужно перезагрузить данные из CSV-файла,
сначала удалите файл db.sqlite3, чтобы уничтожить базу данных.
Затем запустите 'python manage.py migrate' для новой пустой
базы данных с таблицами"""


class Command(BaseCommand):
    help = "Loads data from titles.csv"

    def handle(self, *args, **options):
        if Title.objects.exists():
            print('Данные таблицы titles уже загружены!')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return

        print("Загружаем данные в таблицу titles")
        with open('./static/data/titles.csv', encoding='utf-8') as file:
            data = DictReader(file)
            for row in data:
                category = get_object_or_404(Category, id=row['category'])
                title = Title(
                    id=row['id'],
                    name=row['name'],
                    year=row['year'],
                    category=category
                )
                title.save()
        print("Данные в таблицу title загружены")
