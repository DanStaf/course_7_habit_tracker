from celery import shared_task

from users.services import send_message_to_TG


@shared_task
def send_reminder_to_users():

    send_message_to_TG()

    print('OK')
