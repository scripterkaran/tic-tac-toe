from rest_framework import viewsets
from .models import TicTacToe
from .serializers import TicTacToeSerializer

class TicTacToeViewSet(viewsets.ModelViewSet):
    queryset = TicTacToe.objects.all()
    serializer_class = TicTacToeSerializer