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
    last_move_by = models.ForeignKey(User, null=True, blank=True, related_name='completed_moves')
    is_public = models.BooleanField(default=False)

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

    @classmethod
    def dev_match(cls):
        user_x = User.objects.first()
        game = cls.objects.create(player_x = user_x, created_by=user_x)
        # some one joins a game, and is given two options to select from
        user_y = User.objects.last()
        game.challenge_accepted(user_y,'O')

        # randomly picks who will go first move
        game.mark_move(user_y, 1) # sets the last_moved by:
        game.mark_move(user_x , 2)
        game.mark_move(user_y, 3)
        game.mark_move(user_x, 4)
        game.mark_move(user_y, 5)
        game.mark_move(user_x, 6)
        """
             , o, x
            o, x, o
            x,

        """



    def switch_players(self, last_move_by):
        """
        Games would be sharable, as a user if you create a game, you will be either X or O, and next player would se
        someone who is yet to receive the link(or join a game by clicking on "see open games"). So next_turn_by will be null
        unless some one joins the game. We cannot switch players unless both the players are in.

        when a player's move  is saved, we switch the active(to be played) player.
        :return:
        """
        if not self.player_x or not self.player_o:
            raise ValueError('Switching Player needs 2 players in game.')

        if self.player_x == self.next_turn_by:
            self.next_turn_by = self.player_o
        else:
            self.next_turn_by = self.player_x
        self.save()

    def join_game_(self, user,selection):
        """
        a game is created, and then joined by a user
        :param user:
        :param selection:
        :return:
        """
        if selection == 'X':
            self.player_x = user
        elif selection == 'O':
            self.player_o = user
        return self.save()

    def challenge_accepted(self, user, selection):
        """
        in a situation where a user has created a game, but hasn't selected any of the symbols(X or O). The game creator
        has given the option for other player to select the symbol.When other person selects one of the X or O. The
        game creator will automatically become the counter symbol.
        :param user: session user or normal user
        :return:
        """
        if self.created_by == user:
            return

        if selection == 'X':
            self.player_x = user
            self.player_o = self.created_by
        elif selection == 'O':
            self.player_o = user
            self.player_x = self.created_by
        self.save()


    def auto_assign_symbol_to_challenge_acceptor(self, user):
        """
        in a situation, a game is made public, and the creator has already marked the first move before any one joined
        the game. This function will then auto assign the joiner(the challenge acceptor) to the symbol left between X&O)
        :param user:
        :return:
        """
        if self.created_by == self.player_o:
            self.player_x = user
        else:
            self.player_o = user

    def mark_move(self, user, position):
        if self.last_move_by and self.last_move_by == user:
            return "Cannot make two moves by same user"
        Move.objects.create(game=self, played_by=user, position=position)
        self.last_move_by = user
        self.save()

    def get_other_player(self, user):
        if self.player_o == user:
            return self.player_x
        if self.player_x == user:
            return self.player_o


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
           return self.player_x , "wins the Game"
        elif player_o_moves in winning_moves:
           return self.player_o,  "wins the game"
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

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.game.moves.count() > 9:
            raise ValueError('Maximum Moves per game is achieved.')
        moves_marked = self.game.moves.values_list('position', flat=True)
        if self.position in moves_marked:
            raise ValueError('Move to position {} is already marked.'.format(self.position))
        move = super(Move, self).save()
        return move

    def __unicode__(self):
        return "move by "+ self.played_by.username + " on position" + unicode(self.position)