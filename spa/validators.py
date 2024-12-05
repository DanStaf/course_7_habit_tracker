from rest_framework import serializers

"""
Исключить одновременный выбор связанной привычки и указания вознаграждения.
В модели не должно быть заполнено одновременно и поле вознаграждения,
и поле связанной привычки. Можно заполнить только одно из двух полей.
bonus
bonus_habit

В связанные привычки могут попадать только привычки с признаком приятной привычки.
bonus_habit
is_bonus_habit

У приятной привычки не может быть вознаграждения или связанной привычки.
bonus_habit
bonus_habit
bonus

"""


class MaxValueIntValidator:
    """
    Нельзя выполнять привычку реже, чем 1 раз в 7 дней.
    Нельзя не выполнять привычку более 7 дней.
    Например, привычка может повторяться раз в неделю, но не раз в 2 недели.
    За одну неделю необходимо выполнить привычку хотя бы один раз.
    period_days <= 7

    Время выполнения должно быть не больше 120 секунд.
    duration_sec <= 120

    """

    def __init__(self, field, max_value):
        self.field = field
        self.max_value = max_value

    def __call__(self, value):
        data_value = dict(value).get(self.field)

        if data_value:
            result = data_value <= self.max_value
        else:
            result = True

        # print(f"{data_value} ?<=? {self.max_value} / {result}")

        if not result:
            message = f"Значение {self.field} не должно превышать {self.max_value}"
            raise serializers.ValidationError(message)
