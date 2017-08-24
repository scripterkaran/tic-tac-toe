from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class TicTacToe(models.Model):
    """Defines the players and maintains TicTacToe game.
    """
    player_x = models.ForeignKey(User, related_name="player_x_games") # the player who plays X
    player_o = models.ForeignKey(User, related_name="player_o_games") # the player who plays O
    created = models.DateTimeField(auto_now_add=True)
    stopped = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "game " + unicode(self.id) + " between " + self.player_x.username + " and " + self.player_o.username

class TicTacToeMove(models.Model):
    """ Defines the moves in a single TicTacToe game.
    """
    tic_tac_toe = models.ForeignKey(TicTacToe, related_name="moves")
    position = models.PositiveIntegerField(validators=(MaxValueValidator(int(9)),MinValueValidator(int(0))))
    played_by = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_created=True)
