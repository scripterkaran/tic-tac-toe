from .decorators import allow_lazy_user_view_set
from rest_framework import viewsets
from rest_framework.decorators import detail_route

from .models import Game, Move
from .serializers import GameSerializer, MoveSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    @allow_lazy_user_view_set
    def list(self, request, *args, **kwargs):
        return super(GameViewSet, self).list(request, *args, **kwargs)


class MoveViewSet(viewsets.ModelViewSet):
    queryset = Move.objects.all()
    serializer_class = MoveSerializer


    def get_queryset(self):
        game_pk = self.kwargs.get('game_pk')
        if game_pk:
            return self.queryset.filter(game=game_pk)


    def create(self, request, *args, **kwargs):
        game_instance = self.get_object()
        if game_instance.next_move_by == request.user:
            return super(MoveViewSet, self).create(request, *args,**kwargs)
