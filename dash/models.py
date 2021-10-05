from django.db import models

class Dash(models.Model):
    summary = models.CharField(max_length=200)
