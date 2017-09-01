from rest_framework import serializers
from .models import Game, Move


class MoveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Move
        fields = '__all__'


    def create(self, validated_data):
        validated_data['played_by'] = self.context.get('request').user
        return super(MoveSerializer, self).create(validated_data)


class GameSerializer(serializers.ModelSerializer):
    moves = MoveSerializer(many=True)

    class Meta:
        model  = Game
        fields =('url','player_x', 'player_o', 'is_completed', 'created_by', 'moves')



