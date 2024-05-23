# Dockerfile

# Используйте подходящий базовый образ, например python:3.9
FROM python:3.9

# Установите рабочую директорию
WORKDIR /app

# Скопируйте файлы зависимостей
COPY requirements.txt /app/

# Установите зависимости
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Скопируйте все файлы проекта
COPY . /app/

# Команда по умолчанию для запуска приложения
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
