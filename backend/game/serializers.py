from rest_framework import serializers
from .models import TicTacToe, TicTacToeMove


class TicTacToeSerializer(serializers.ModelSerializer):

    class Meta:
        model  = TicTacToe
        fields =('url','player_x', 'player_o', 'is_completed', 'created_by')


class TicTacToeMoveSerializer(serializers.ModelSerializer):

    class Meta:
        model = TicTacToeMove
        fields = '__all__'
