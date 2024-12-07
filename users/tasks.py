from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from spa.models import Habit
from users.services import send_messages_to_TG


@shared_task
def send_reminder_to_users():

    habits = Habit.objects.filter(is_bonus_habit=False)

    today_habits = []
    today_date = timezone.datetime.today().date()

    for habit in habits:

        message = f'{habit.last_execution_date}'

        if not habit.last_execution_date:
            to_do = True
            message += ' - new task executed first time'
        else:
            if not habit.period_days:
                message += ' - period_days not filled'
                to_do = False
            else:
                next_execution_date = habit.last_execution_date + timedelta(days=habit.period_days)
                to_do = next_execution_date == today_date  # True, False
                message += f" / {next_execution_date} = {today_date} / {to_do}"

        # print(message)

        if to_do:
            if habit.user.tg_id == 1:
                message = f"Пользователь {habit.user} не заполнил Telegram ID"
                print(message)
            else:
                habit.last_execution_date = today_date
                habit.save()
                today_habits.append(habit)

    send_messages_to_TG(today_habits)

    print("Reminder done")

    # [print(f"{item} / {item.last_execution_date} / {item.time}") for item in today_habits]
