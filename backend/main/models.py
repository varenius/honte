from django.db import models

# Create your models here.
class Player(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    rating = models.IntegerField()
    egd_pin = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Game(models.Model):
    class Results(models.TextChoices):
        NOT_PLAYED = 'NP', 'Not played'
        TIED = 'T', 'Tied'
        WON = 'W', 'Won'
        WO = 'WO', 'Walk over'

    player1 = models.ForeignKey('Player', on_delete=models.PROTECT, related_name='game_player1')
    player2 = models.ForeignKey('Player', on_delete=models.PROTECT, related_name='game_player2', null=True)
    result = models.CharField(choices=Results.choices, max_length=2)
    winner = models.ForeignKey('Player', on_delete=models.PROTECT, related_name='game_winner', null=True)
