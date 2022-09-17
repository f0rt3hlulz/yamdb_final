from csv import DictReader
from django.core.management import BaseCommand
from django.shortcuts import get_object_or_404

from reviews.models import Review, User, Title


ALREDY_LOADED_ERROR_MESSAGE = """
Если вам нужно перезагрузить данные из CSV-файла,
сначала удалите файл db.sqlite3, чтобы уничтожить базу данных.
Затем запустите 'python manage.py migrate' для новой пустой
базы данных с таблицами"""


class Command(BaseCommand):
    help = "Loads data from review.csv"

    def handle(self, *args, **options):
        if Review.objects.exists():
            print('Данные таблицы review уже загружены!')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return

        print("Загружаем данные в таблицу review")
        with open('./static/data/review.csv', encoding='utf-8') as file:
            data = DictReader(file)
            for row in data:
                author = get_object_or_404(User, id=row['author'])
                title = get_object_or_404(Title, id=row['title_id'])
                review = Review(
                    id=row['id'],
                    title=title,
                    text=row['text'],
                    author=author,
                    score=row['score'],
                    pub_date=row['pub_date']
                )
                review.save()
        print("Данные в таблицу review загружены")
