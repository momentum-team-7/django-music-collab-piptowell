from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Album(models.Model):
    title = models.CharField(max_length=280)
    artist = models.CharField(max_length=280)
    release_date = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="albums")

    def __str__(self):
        return self.title


class Artist(models.Model):
    artist = models.CharField(max_length=280)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, blank=True, null=True, related_name="artists")

    def __str__(self):
        return self.artist
