![Build Status](https://travis-ci.com/f0rt3hlulz/api_yamdb.svg?branch=master)](https://travis-ci.com/f0rt3hlulz/api_yamdb)
![Yamdb-app_workflow](https://github.com/f0rt3hlulz/yamdb_final/workflows/Yamdb-app_workflow/badge.svg)

![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)
![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

## Стек технологий в проекте:
- Python
- Dajngo
- REST API
- PostgreSQL
- nginx
- Docker

API развернут по адресу http://84.201.160.177/api/v1/

# REST API для сервиса **YamDb** 
версия c Docker, Continuous Integration на GitHub Actions

## База отзывов о фильмах, книгах и музыке. 

## Описание

Проект **YaMDb** собирает отзывы пользователей на произведения. 
Произведения делятся на категории: «Книги», «Фильмы», «Музыка». 
Список категорий (Category) может быть расширен (например, можно добавить категорию 
«Изобразительное искусство» или «Ювелирка» через интерфейс Django администратора).

### API для сервиса YaMDb 
позволяет работать со следующими сущностями:

**Пользователи** (Получить список всех пользователей, создание пользователя, получить пользователя по username, изменить данные пользователя по username, удалить пользователя по username, получить данные своей учетной записи, изменить данные своей учетной записи)

**Произведения**, к которым пишут отзывы (Получить список всех объектов, создать произведение для отзывов, информация об объекте, обновить информацию об объекте, удалить произведение)

**Категории** (типы) произведений (Получить список всех категорий, создать категорию, удалить категорию)

**Жанры** (Получить список всех жанров, создать жанр, удалить жанр)

**Отзывы** (Получить список всех отзывов, создать новый отзыв, получить отзыв по id, частично обновить отзыв по id, удалить отзыв по id)

**Коментарии к отзывам** (Получить список всех комментариев к отзыву по id, создать новый комментарий для отзыва, получить комментарий для отзыва по id, частично обновить комментарий к отзыву по id, удалить комментарий к отзыву по id)

**JWT-токен** (Отправление confirmation_code на переданный email, получение JWT-токена в обмен на email и confirmation_code)

### Алгоритм регистрации пользователей

* Пользователь отправляет запрос с параметром email на /auth/email/.
* YaMDB отправляет письмо с кодом подтверждения (confirmation_code) на адрес email .
* Пользователь отправляет запрос с параметрами email и confirmation_code на /auth/token/, в ответе на запрос ему приходит token (JWT-токен).
* При желании пользователь отправляет PATCH-запрос на /users/me/ и заполняет поля в своём профайле (описание полей — в документации).
[Полная документация API (redoc.yaml)](https://github.com/BolshakovAndrey/api_yamdb/blob/master/static/redoc.yaml)

## Установка на локальном компьютере
Эти инструкции помогут вам создать копию проекта и запустить ее на локальном компьютере для целей разработки и тестирования.

### Установка Docker
Установите Docker, используя инструкции с официального сайта:
- для [Linux](https://docs.docker.com/engine/install/ubuntu/). Отдельно потребуется установть [Docker Compose](https://docs.docker.com/compose/install/)

### Запуск проекта (на примере Linux)

- Создайте на своем компютере папку проекта YamDb `mkdir yamdb` и перейдите в нее `cd yamdb`
- Склонируйте этот репозиторий в текущую папку `git clone https://github.com/f0rt3hlulz/yamdb_final/ .`
- Создайте файл `.env` командой `touch .env` и добавьте в него переменные окружения для работы с базой данных:
```
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД 
```
- Запустите docker-compose командой `sudo docker-compose up -d`
- Накатите миграции `sudo docker-compose exec yamdb python manage.py migrate`
- Соберите статику командой `sudo docker-compose exec yamdb python manage.py collectstatic --no-input`
- Создайте суперпользователя Django `sudo docker-compose exec yamdb python manage.py createsuperuser --username admin --email 'admin@yamdb.com'`
- Загрузите данные в базу данных при необходимости `sudo docker-compose exec yamdb python manage.py loaddata data/fixtures.json`
## Деплой на удаленный сервер
Для запуска проекта на удаленном сервере необходимо:
- скопировать на сервер файлы `docker-compose.yaml`, `.env` и папку `nginx` командами:
```
scp docker-compose.yaml  <user>@<server-ip>:
scp .env <user>@<server-ip>:
scp -r nginx/ <user>@<server-ip>:

```
- создать переменные окружения в разделе `secrets` настроек текущего репозитория:
```
DOCKER_PASSWORD # Пароль от Docker Hub
DOCKER_USERNAME # Логин от Docker Hub
HOST # Публичный ip адрес сервера
USER # Пользователь зарегистрированный на сервере
PASSPHRASE # Если ssh-ключ защищен фразой-паролем
SSH_KEY # Приватный ssh-ключ
TELEGRAM_TO # ID телеграм-аккаунта
TELEGRAM_TOKEN # Токен бота
```

### После каждого обновления репозитория (`git push`) будет происходить:
1. Проверка кода на соответствие стандарту PEP8 (с помощью пакета flake8) и запуск pytest из репозитория yamdb_final
2. Сборка и доставка докер-образов на Docker Hub.
3. Автоматический деплой.
4. Отправка уведомления в Telegram.

### Примеры эндпоинтов:

Регистрация нового пользователя
Получить код подтверждения на переданный email.
Права доступа: Доступно без токена.

```
http://127.0.0.1:8000/api/v1/auth/signup/
```

Получение JWT-токена
Получение JWT-токена в обмен на username и confirmation code.
Права доступа: Доступно без токена.

```
http://127.0.0.1:8000/api/v1/auth/signup/
```

Получение списка всех категорий
Получить список всех категорий
Права доступа: Доступно без токена

```
http://127.0.0.1:8000/api/v1/categories/
```

Добавление новой категории
Создать категорию.
Права доступа: Администратор.

```
http://127.0.0.1:8000/api/v1/categories/
```

Удаление категории
Удалить категорию.
Права доступа: Администратор.

```
http://127.0.0.1:8000/api/v1/categories/{slug}/
```

Подробнее можно посмотреть в документации Redoc после старта сервера по адресу:

```
http://127.0.0.1:8000/redoc/
```

### Разработчик:

[Илья Ярцев](https://github.com/f0rt3hlulz)