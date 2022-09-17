from csv import DictReader
from django.core.management import BaseCommand

from reviews.models import Category


ALREADY_LOADED_ERROR_MESSAGE = """
Если вам нужно перезагрузить данные из CSV-файла,
сначала удалите файл db.sqlite3, чтобы уничтожить базу данных.
Затем запустите 'python manage.py migrate' для новой пустой
базы данных с таблицами"""


class Command(BaseCommand):
    help = "Loads data from category.csv"

    def handle(self, *args, **options):
        if Category.objects.exists():
            print('Данные таблицы category уже загружены!')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return

        print("Загружаем данные в таблицу category")
        with open('./static/data/category.csv', encoding='utf-8') as file:
            data = DictReader(file)
            for row in data:
                category = Category(
                    id=row['id'],
                    name=row['name'],
                    slug=row['slug'],
                )
                category.save()
        print("Данные в таблицу category загружены")
