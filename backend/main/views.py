from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
import random

from .models import Player
from .models import Game
from .serializers import PlayerSerializer
from .serializers import GameSerializer
from django.http import HttpResponse
from .name_generator import get_name


class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows players to be viewed or edited.
    """
    queryset = Player.objects.all().order_by('rating')
    serializer_class = PlayerSerializer


class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows games to be viewed or edited.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer



def add_player(request):
    player = Player()
    player.first_name, player.last_name = get_name(False)
    player.rating = 1000
    player.egd_pin = random.randint(10000, 100000)
    player.save()
    return HttpResponse(200)


@api_view(['GET'])
def add_game(request):
    all_players = Player.objects.values_list('pk', flat=True)
    player1_pk, player2_pk = random.choices(population=all_players, k=2)
    player1 = Player.objects.get(pk=player1_pk)
    player2 = Player.objects.get(pk=player2_pk)
    result=random.choice(Game.Results.choices)
    result_id, _ = result
    winner = None
    if result_id == Game.Results.WON:
        winner = random.choice([player1, player2])
    game = Game.objects.create(player1=player1, player2=player2, result=result, winner=winner)
    return Response(GameSerializer(game, context={'request': request}).data)
