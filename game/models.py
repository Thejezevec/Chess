from django.db import models

class Game(models.Model):
    #players
    player_white = models.CharField(max_length=100, default='white')
    player_black = models.CharField(max_length=100, default='black')
    #game state
    is_draw = models.BooleanField(default=False)
    winner = models.BooleanField(max_length=100, choices=[('white', 'White'), ('black', 'Black')], null=True, blank= True)
    #board state
    board_state = models.CharField(max_length=300)

    def __str__(self):
        return f"game {self.player_white} vs {self.player_black}"
