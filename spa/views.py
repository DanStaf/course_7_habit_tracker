import rest_framework.permissions
from django.shortcuts import render
from rest_framework import viewsets

from spa.models import Habit
from spa.paginators import MyPagination
from spa.serializers import HabitSerializer
from users.permissions import IsOwnerClass


class HabitViewSet(viewsets.ModelViewSet):
    """
    owner can view their own list and retrieve
    owner can update and delete
    all can create
    """

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
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsOwnerClass]

        return super().get_permissions()


class PublicViewSet(viewsets.ModelViewSet):
    """
    all can view list and retrieve
    owner can update and delete
    no one can create
    """
    serializer_class = HabitSerializer
    pagination_class = MyPagination

    def get_queryset(self):
        queryset = Habit.objects.filter(is_public=True)
        return queryset

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsOwnerClass]
        elif self.action in ['create']:
            self.permission_classes = [~rest_framework.permissions.AllowAny]

        return super().get_permissions()
