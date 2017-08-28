from rest_framework import serializers
from .models import Game, Move


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model  = Game
        fields =('url','player_x', 'player_o', 'is_completed', 'created_by')


class MoveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Move
        fields = '__all__'
