from rest_framework import viewsets
from .models import TicTacToe, TicTacToeMove
from .serializers import TicTacToeSerializer, TicTacToeMoveSerializer


class TicTacToeViewSet(viewsets.ModelViewSet):
    queryset = TicTacToe.objects.all()
    serializer_class = TicTacToeSerializer

class TicTacToeMoveViewSet(viewsets.ModelViewSet):
    queryset = TicTacToeMove.objects.all()
    serializer_class = TicTacToeMoveSerializer