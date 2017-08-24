from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class TicTacToe(models.Model):
    """Defines the players and maintains TicTacToe game.
    """
    player_x = models.ForeignKey(User) # the player who plays X
    player_o = models.ForeignKey(User) # the player who plays O
    created = models.DateTimeField(auto_created=True)
    stopped = models.DateTimeField(auto_now_add=True)

class TicTacToeMove(models.Model):
    """ Defines the moves in a single TicTacToe game.
    """
    tic_tac_toe = models.ForeignKey(TicTacToe, related_name="moves")
    position = models.PositiveIntegerField(validators=(MaxValueValidator(int(9)),MinValueValidator(int(0))))
    played_by = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_created=True)
