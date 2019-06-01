from django.db import models


class Artists(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Album(models.Model):
    artists = models.ForeignKey(Artists, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
