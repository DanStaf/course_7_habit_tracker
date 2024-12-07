from django.db import models

from users.models import User


class Habit(models.Model):
    """
    я буду [ДЕЙСТВИЕ] в [ВРЕМЯ] в [МЕСТО]
    I will do [action] in [time] at [place]
    """

    user = models.ForeignKey(User, verbose_name='Владелец', on_delete=models.CASCADE)
    action = models.CharField(max_length=150, verbose_name='Действие (описание привычки)')

    is_bonus_habit = models.BooleanField(default=False, verbose_name='Признак приятной привычки')
    bonus = models.CharField(null=True, blank=True, max_length=150, verbose_name='Вознаграждение (описание)')
    bonus_habit = models.ForeignKey("spa.Habit",
                                    null=True, blank=True,
                                    verbose_name='Связанная привычка',
                                    on_delete=models.SET_NULL)

    place = models.CharField(null=True, blank=True, max_length=150, verbose_name='Место')
    time = models.TimeField(null=True, blank=True, verbose_name='Время')
    period_days = models.PositiveIntegerField(null=True, blank=True, verbose_name='Периодичность (в днях)')
    duration_sec = models.PositiveIntegerField(null=True, blank=True, verbose_name='Время на выполнение (в секундах)')

    is_public = models.BooleanField(default=False, verbose_name='Признак публичности')

    last_execution_date = models.DateField(null=True, blank=True, verbose_name='Дата последнего выполнения')

    def __str__(self):
        return f'Habit: {self.action}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
