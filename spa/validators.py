from rest_framework import serializers


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
            message = (f"Значение {self.field} не должно "
                       f"превышать {self.max_value}")
            raise serializers.ValidationError(message)


def is_bonus_valid(is_bonus_habit, bonus_habit, bonus):
    """
    Исключить одновременный выбор связанной привычки и указания вознаграждения.
    В модели не должно быть заполнено одновременно и поле вознаграждения,
    и поле связанной привычки. Можно заполнить только одно из двух полей.
    bonus
    bonus_habit

    В связанные привычки могут попадать только привычки
    с признаком приятной привычки.
    bonus_habit
    is_bonus_habit

    У приятной привычки не может быть вознаграждения или связанной привычки.
    is_bonus_habit
    bonus_habit
    bonus

    """

    if is_bonus_habit:
        if bonus_habit or bonus:
            message = ("У приятной привычки не может быть вознаграждения"
                       " или связанной привычки.")
            raise serializers.ValidationError(message)
    else:
        if bonus and bonus_habit:
            message = ("Можно заполнить только одно из двух полей "
                       "(вознаграждение либо связанную привычку).")
            raise serializers.ValidationError(message)

        if bonus_habit and not bonus_habit.is_bonus_habit:
            message = ("В связанные привычки могут попадать только привычки"
                       " с признаком приятной привычки.")
            raise serializers.ValidationError(message)

        if not bonus and not bonus_habit:
            message = ("Необходимо заполнить одно из полей: вознаграждение, "
                       "или связанную привычку, или признак приятной привычки")
            raise serializers.ValidationError(message)

    # print("bonus is valid")
