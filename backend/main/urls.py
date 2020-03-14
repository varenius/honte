from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register(r'players', views.PlayerViewSet)
router.register(r'games', views.GameViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('add_player', views.add_player),
    path('add_game', views.add_game)
]
