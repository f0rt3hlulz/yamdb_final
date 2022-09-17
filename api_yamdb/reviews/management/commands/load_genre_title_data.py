from csv import DictReader

from django.core.management import BaseCommand
from django.shortcuts import get_object_or_404
from reviews.models import Genre, GenreTitle, Title

ALREDY_LOADED_ERROR_MESSAGE = """
Если вам нужно перезагрузить данные из CSV-файла,
сначала удалите файл db.sqlite3, чтобы уничтожить базу данных.
Затем запустите 'python manage.py migrate' для новой пустой
базы данных с таблицами"""


class Command(BaseCommand):
    help = "Loads data from genre_title.csv"

    def handle(self, *args, **options):
        if GenreTitle.objects.exists():
            print('Данные таблицы genre_title уже загружены!')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return

        print("Загружаем данные в таблицу genre_title")
        with open('./static/data/genre_title.csv', encoding='utf-8') as file:
            data = DictReader(file)
            for row in data:
                genre = get_object_or_404(Genre, id=row['genre_id'])
                title = get_object_or_404(Title, id=row['title_id'])
                genre_title = GenreTitle(
                    id=row['id'],
                    title=title,
                    genre=genre
                )
                genre_title.save()
        print("Данные в таблицу genre_title загружены")
