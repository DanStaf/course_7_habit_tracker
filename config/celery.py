from __future__ import absolute_import
import os
from datetime import timedelta

from celery import Celery

# Установка переменной окружения для настроек проекта
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Создание экземпляра объекта Celery
app = Celery('config')

# Загрузка настроек из файла Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматическое обнаружение и регистрация задач из файлов tasks.py в приложениях Django
app.autodiscover_tasks()


app.conf.update(
    CELERYBEAT_SCHEDULE={
        'send_reminder_to_users': {
            'task': 'users.tasks.send_reminder_to_users',  # Путь к задаче
            'schedule': timedelta(seconds=10),  # Расписание выполнения задачи
        },
    }
)
