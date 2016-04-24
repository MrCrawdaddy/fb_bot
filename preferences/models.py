from django.db import models
from django.contrib.auth.models import User


class SubChoice(models.Model):
    name = models.CharField(max_length=30)
    url = models.URLField()

    def __str__(self):
        return self.name


class UserPreferences(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    sub = models.ManyToManyField(SubChoice)
    time = models.IntegerField(default=1)
