from django.db import models


class post(models.Model):

    nameOfPoster = models.CharField(max_length=100)
    nameOfLocation = models.CharField(max_length=100)
    photoURL = models.TextField()
    Description = models.TextField()
