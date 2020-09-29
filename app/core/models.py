import uuid
import os
from django.db import models
from django.conf import settings

class Playerstats(models.Model):

    ball_number = models.CharField(max_length=255)
    bowler_name = models.CharField(max_length=255)
    batsman_name = models.CharField(max_length=255)
    non_striker_name = models.CharField(max_length=255)
    run_batsman = models.CharField(max_length=255)

    def __str__(self):
        return self.name
