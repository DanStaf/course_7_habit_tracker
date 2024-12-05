from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from spa.models import Habit
from spa.validators import MaxValueIntValidator


class HabitSerializer(ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            MaxValueIntValidator(field='period_days', max_value=7),
            MaxValueIntValidator(field='duration_sec', max_value=120)
        ]
