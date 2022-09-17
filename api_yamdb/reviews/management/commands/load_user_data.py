from csv import DictReader
from django.core.management import BaseCommand

from reviews.models import User


ALREDY_LOADED_ERROR_MESSAGE = """
Если вам нужно перезагрузить данные из CSV-файла,
сначала удалите файл db.sqlite3, чтобы уничтожить базу данных.
Затем запустите 'python manage.py migrate' для новой пустой
базы данных с таблицами"""


class Command(BaseCommand):
    help = "Loads data from users.csv"

    def handle(self, *args, **options):
        if User.objects.exists():
            print('Данные таблицы users уже загружены!')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return

        print("Загружаем данные в таблицу users")
        with open('./static/data/users.csv', encoding='utf-8') as file:
            data = DictReader(file)
            for row in data:
                user = User(
                    id=row['id'],
                    username=row['username'],
                    email=row['email'],
                    role=row['role'],
                    bio=row['bio'],
                    first_name=row['first_name'],
                    last_name=row['last_name']
                )
                user.save()
        print("Данные в таблицу user загружены")
