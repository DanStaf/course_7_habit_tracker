from rest_framework.serializers import ModelSerializer

from spa.models import Habit
from spa.validators import MaxValueIntValidator, is_bonus_valid


class HabitSerializer(ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            MaxValueIntValidator(field='period_days', max_value=7),
            MaxValueIntValidator(field='duration_sec', max_value=120)
        ]

    def validate(self, attrs):
        """
        1) compare old and new data. Get the final one.
        2) validate the final data.

        :param:
        self: self.instance is Habit obj.
        attrs: dict with new data from request,
        e.g.: attrs = {'period_days': 4}

        :return:
        attrs if data is valid
        """

        is_bonus_habit = self._get_actual_value_for_validation(
            attrs,
            "is_bonus_habit"
        )
        bonus_habit = self._get_actual_value_for_validation(
            attrs,
            "bonus_habit"
        )
        bonus = self._get_actual_value_for_validation(attrs, "bonus")

        is_bonus_valid(is_bonus_habit, bonus_habit, bonus)

        return attrs

    def _get_actual_value_for_validation(self, data_dict, key):
        """
        1) return new value
        2) if not exist return old value
        3) if not exist return None

        :param data_dict:
        :param key:
        :return:
        """

        instance_habit = self.instance

        if key in data_dict:
            # если в словаре есть новое значение
            value = data_dict.get(key)

        elif instance_habit is None:
            # если нет нового значения
            # и нет старого значение
            value = None

        else:
            # если нет нового значения
            # но есть старое значение
            value = getattr(instance_habit, key)  # == instance_habit."key"

        # print(value)

        return value
