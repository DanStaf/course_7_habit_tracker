from django.urls import path, include
from rest_framework import routers

from spa.apps import SpaConfig
from spa.views import HabitViewSet, PublicViewSet

app_name = SpaConfig.name

router_habit = routers.DefaultRouter()
router_habit.register(r'habits', HabitViewSet, basename='habit')
router_habit.register(r'public', PublicViewSet, basename='public')

urlpatterns = [
    path('', include(router_habit.urls)),
]
