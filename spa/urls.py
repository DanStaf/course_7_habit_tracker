from django.urls import path, include
from rest_framework import routers

from spa.apps import SpaConfig
from spa.views import HabitViewSet

app_name = SpaConfig.name

router_habit = routers.DefaultRouter()
router_habit.register(r'habits', HabitViewSet, basename='habit')

urlpatterns = [
    path('', include(router_habit.urls)),
]
