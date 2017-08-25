from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TicTacToe(TimeStampedModel):
    """Defines the players and maintains TicTacToe game.
    """
    player_x = models.ForeignKey(User, related_name="player_x_games", null=True, blank=True) # the player who plays X
    player_o = models.ForeignKey(User, related_name="player_o_games", null=True, blank=True) # the player who plays O
    created_by = models.ForeignKey(User, related_name='created_games', null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    stopped = models.DateTimeField(auto_now=True) # why do you need this ?


    def __unicode__(self):
        return "game " + unicode(self.id) + " between " + self.player_x.username + " and " + self.player_o.username

class TicTacToeMove(TimeStampedModel):
    """ Defines the moves in a single TicTacToe game.
    """
    tic_tac_toe = models.ForeignKey(TicTacToe, related_name="moves")
    played_by = models.ForeignKey(User)
    position = models.PositiveIntegerField(validators=(MaxValueValidator(int(9)),MinValueValidator(int(0))))
