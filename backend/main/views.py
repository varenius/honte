from rest_framework import viewsets
import random

from .models import Player
from .serializers import PlayerSerializer
from django.http import HttpResponse
from .name_generator import get_name


class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows players to be viewed or edited.
    """
    queryset = Player.objects.all().order_by('rating')
    serializer_class = PlayerSerializer


def add_player(request):
    player = Player()
    player.first_name, player.last_name = get_name(False)
    player.rating = 1000
    player.egd_pin = random.randint(10000, 100000)
    player.save()
    return HttpResponse(200)
