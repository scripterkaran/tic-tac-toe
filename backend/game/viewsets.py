from rest_framework import viewsets
from rest_framework.decorators import detail_route

from .models import Game, Move
from .serializers import GameSerializer, MoveSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class MoveViewSet(viewsets.ModelViewSet):
    queryset = Move.objects.all()
    serializer_class = MoveSerializer


    def get_queryset(self):
        game_pk = self.kwargs.get('game_pk')
        if game_pk:
            return self.queryset.filter(game=game_pk)
