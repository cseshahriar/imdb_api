from django.db import models


class Movie(models.Model):
    """ Movie model """
    name = models.CharField(max_length=100)
    description = models.TextField()
    active = models.BooleanField()

    def __str__(self):
        return self.name