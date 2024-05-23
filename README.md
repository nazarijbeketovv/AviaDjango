# Система Бронирования Билетов

![Django](https://img.shields.io/badge/Django-3.2-blue)
![Celery](https://img.shields.io/badge/Celery-5.2.3-brightgreen)
![Redis](https://img.shields.io/badge/Redis-7.2.4-red)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14.6-blue)
![Docker](https://img.shields.io/badge/Docker-3.8-blue)

Система бронирования билетов - это веб-приложение, которое позволяет пользователям бронировать билеты на авиарейсы. Этот проект использует Django для бэкенда, Celery для управления задачами, Redis как брокер сообщений и PostgreSQL в качестве базы данных. Docker используется для контейнеризации приложения.

## Используемые технологии

- **Django** - Веб-фреймворк
- **Celery** - Распределенная очередь задач
- **Redis** - Хранилище данных в памяти, используемое как брокер сообщений для Celery
- **PostgreSQL** - Реляционная база данных
- **Docker** - Платформа для контейнеризации

## Предварительные требования

Перед началом работы убедитесь, что у вас установлены следующие инструменты:

- Docker: [Установить Docker](https://docs.docker.com/get-docker/)


## Начало работы

### Клонирование репозитория

```sh
git clone https://github.com/nazarijbeketovv/AviaDjango.git
cd AviaDjango
```

### Создание и настройка переменных окружения
Создайте файл .env в корневом каталоге проекта на основе предоставленного шаблона .env.template:

```python
# SMTPYANDEX
EMAIL_HOST=smtp.yandex.ru
EMAIL_PORT=465
EMAIL_HOST_USER=LHbI4@example.com
EMAIL_HOST_PASSWORD=password222
EMAIL_USE_SSL=True

# Django
SECRET_KEY=secret
DEBUG=1

# PostgreSQL
DB_NAME=dbname
DB_USER=dbuser
DB_PASSWORD=pass
DB_HOST=database
DB_PORT=5432
```

### Сборка и запуск приложения с помощью Docker Compose:

```sh
docker-compose up --build
```
### Эта команда выполнит следующие действия:

Соберет образы Docker для сервисов app, worker и flower.
Запустит контейнеры для PostgreSQL, Redis и приложения Django.
Применит миграции базы данных.
Запустит сервер разработки Django на http://localhost:8000.
Доступ к сервисам
Приложение Django: http://localhost:8000
Панель Flower (инструмент мониторинга Celery): http://localhost:5555
Запуск задач Celery
Рабочий процесс Celery настроен для запуска как отдельный сервис в файле docker-compose.yml и будет автоматически запущен вместе с приложением. Celery используется для обработки фоновых задач, таких как отправка электронных писем.

### Использование:

После запуска приложения вы можете:

Открыть http://localhost:8000 в вашем веб-браузере.
Зарегистрировать новую учетную запись.
Забронировать билеты на авиарейсы.
Проверить вашу электронную почту для получения информации о билетах.


### Остановка приложения

Чтобы остановить приложение, выполните команду:

```sh
docker-compose down
```

Эта команда остановит и удалит контейнеры, определенные в docker-compose.yml.

