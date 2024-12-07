from config.settings import TG_API_KEY

import telebot

telebot.apihelper.ENABLE_MIDDLEWARE = True


def send_messages_to_TG(today_habits):

    bot = telebot.TeleBot(TG_API_KEY)

    for habit in today_habits:
        message = f"Напоминание! Привычку '{habit}' нужно выполнить сегодня в {habit.time}"
        bot.send_message(habit.user.tg_id, message)
