from csv import DictReader

from django.core.management import BaseCommand
from django.shortcuts import get_object_or_404
from reviews.models import Comment, Review, User

ALREDY_LOADED_ERROR_MESSAGE = """
Если вам нужно перезагрузить данные из CSV-файла,
сначала удалите файл db.sqlite3, чтобы уничтожить базу данных.
Затем запустите 'python manage.py migrate' для новой пустой
базы данных с таблицами"""


class Command(BaseCommand):
    help = "Loads data from comment.csv"

    def handle(self, *args, **options):
        if Comment.objects.exists():
            print('Данные таблицы comment уже загружены!')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return

        print("Загружаем данные в таблицу comment")
        with open('./static/data/comments.csv', encoding='utf-8') as file:
            data = DictReader(file)
            for row in data:
                author = get_object_or_404(User, id=row['author'])
                review = get_object_or_404(Review, id=row['review_id'])
                comment = Comment(
                    id=row['id'],
                    review=review,
                    text=row['text'],
                    author=author,
                    pub_date=row['pub_date']
                )
                comment.save()
        print("Данные в таблицу comment загружены")
