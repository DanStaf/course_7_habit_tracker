from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

# from online_learning.validators import TextValidator

from spa.models import Habit


class HabitSerializer(ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        # validators = [TextValidator(field='url', correct_text='youtube.com')]
