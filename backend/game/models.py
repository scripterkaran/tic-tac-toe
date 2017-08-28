from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from .utils import *

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Game(TimeStampedModel):
    """Defines the players and maintains TicTacToe game.
    """
    player_x = models.ForeignKey(User, related_name="player_x_games", null=True, blank=True) # the player who plays X
    player_o = models.ForeignKey(User, related_name="player_o_games", null=True, blank=True) # the player who plays O
    created_by = models.ForeignKey(User, related_name='created_games', null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    stopped = models.DateTimeField(auto_now=True) # why do you need this ? to record the time of the game


    def __unicode__(self):
        return "game " + unicode(self.id) + " between " + self.player_x.username + " and " + self.player_o.username

    def get_moves_by_player(self, player):
        moves = player.moves.all().values_list('position')
        pos = ()
        for m in moves:
            pos = pos + get_coordinates_by_position(m)
        return pos

    def get_player_x_moves(self):
        return set(self.get_moves_by_player(self.player_x))

    def get_player_o_moves(self):
        return set(self.get_moves_by_player(self.player_o))

    def game_over(self):
        if not self.winner():
           return False
        return True

    def next_player(self):
        pass

    def winner(self):
        """
        fetches the moves of each player and finds an intersection with winning moves
        :return: statements if match is over and either of the player has won or not
                 False if game is still on
        """
        player_x_moves = self.get_player_x_moves()
        player_o_moves = self.get_player_o_moves()
        winning_moves = generate_winning_positions()
        if player_x_moves in winning_moves:
           return "Player X wins the game"
        elif player_o_moves in winning_moves:
           return "Player O wins the game"
        else:
           if self.moves.count() == 9:
              return "Its a tie"
        return False

class Move(TimeStampedModel):
    """ Defines the moves in a single TicTacToe game.
    """
    game = models.ForeignKey(Game, related_name="moves")
    played_by = models.ForeignKey(User, related_name="moves")
    position = models.PositiveIntegerField(validators=(MaxValueValidator(int(8)),MinValueValidator(int(0))))

    def __unicode__(self):
        return "move by "+ self.played_by.username + " on position" + unicode(self.position)