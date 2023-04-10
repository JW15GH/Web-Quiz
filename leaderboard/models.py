from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Score(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.player.username}: {self.score}"
