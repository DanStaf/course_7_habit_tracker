from django.shortcuts import render
from rest_framework import viewsets

from spa.models import Habit
from spa.paginators import MyPagination
from spa.serializers import HabitSerializer
from users.permissions import IsOwnerClass


# Create your views here.


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    pagination_class = MyPagination

    def get_queryset(self):
        queryset = Habit.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        new_instance = serializer.save()
        new_instance.user = self.request.user
        new_instance.save()

    def get_permissions(self):
        if self.action in ['update', 'destroy']:
            self.permission_classes = [IsOwnerClass]

        return super().get_permissions()
