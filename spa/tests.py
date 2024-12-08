from django.urls import reverse

from rest_framework.test import APITestCase

from spa.models import Habit
from users.models import User

from rest_framework import status


class HabitTestCase(APITestCase):

    def setUp(self):
        # Подготовка данных перед каждым тестом
        self.user = User.objects.create(
            email='test_user@test_user.ru',
            tg_id=111,
            first_name='test_user',
            last_name='test_user',
            is_staff=False,
            is_superuser=False
        )
        self.habit = Habit.objects.create(
            user=self.user,
            action='test_action',
            is_bonus_habit=True
        )
        self.client.force_authenticate(user=self.user)

    def test_retrieve(self):
        url = reverse('spa:habit-detail', args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('action'), self.habit.action)

    def test_create(self):
        new_text = 'test_action_2'
        url = reverse('spa:habit-list')
        data = {
            'action': new_text,
            'is_bonus_habit': True,
            'user': self.user.pk,
            'period_days': 2,
            'duration_sec': 20
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)
        self.assertEqual(Habit.objects.get(action=new_text).user, self.user)
        self.assertEqual(Habit.objects.get(action=new_text).period_days, 2)
        self.assertEqual(Habit.objects.get(action=new_text).duration_sec, 20)

        """
        Значение {self.field} не должно превышать {self.max_value}
        """

        new_text = 'test_action_3'
        url = reverse('spa:habit-list')
        data = {
            'action': new_text,
            'is_bonus_habit': True,
            'user': self.user.pk,
            'duration_sec': 2000
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        """
        Необходимо заполнить одно из полей:
        вознаграждение, или связанную привычку,
        или признак приятной привычки.
        """

        new_text = 'test_action_4'
        url = reverse('spa:habit-list')
        data = {
            'action': new_text,
            'user': self.user.pk
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        """
        У приятной привычки не может быть вознаграждения
        или связанной привычки.
        """

        new_text = 'test_action_5'
        url = reverse('spa:habit-list')
        data = {
            'action': new_text,
            'user': self.user.pk,
            'is_bonus_habit': True,
            'bonus': 'TEST_BONUS'
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        """
        В связанные привычки могут попадать только привычки
        с признаком приятной привычки.
        """

        new_text = 'test_action_6'
        url = reverse('spa:habit-list')
        data = {
            'action': new_text,
            'user': self.user.pk,
            'bonus_habit': self.habit.pk
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        """
        Можно заполнить только одно из двух полей
        (вознаграждение либо связанную привычку).
        """

        new_text = 'test_action_6'
        url = reverse('spa:habit-list')
        data = {
            'action': new_text,
            'user': self.user.pk,
            'bonus_habit': self.habit.pk,
            'bonus': 'TEST_BONUS'
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update(self):
        new_text = 'test_action_updated'
        url = reverse('spa:habit-detail', args=(self.habit.pk,))
        data = {'action': new_text}
        response = self.client.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('action'), new_text)

    def test_delete(self):

        url = reverse('spa:habit-detail', args=(self.habit.pk,))

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_list(self):
        url = reverse('spa:habit-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.data,
            {
                'count': 1,
                'next': None,
                'previous': None,
                'results':
                    [
                        {
                            'id': self.habit.pk,
                            'action': self.habit.action,
                            'is_bonus_habit': self.habit.is_bonus_habit,
                            'bonus': self.habit.bonus,
                            'place': self.habit.place,
                            'time': self.habit.time,
                            'period_days': self.habit.period_days,
                            'duration_sec': self.habit.duration_sec,
                            'is_public': self.habit.is_public,
                            'last_execution_date':
                                self.habit.last_execution_date,
                            'user': self.habit.user.pk,
                            'bonus_habit': self.habit.bonus_habit
                        }
                    ]
            }

        )
