from django.db import models
from django.contrib.auth.models import User


class UserTimePreference(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE)

    time = models.IntegerField(default=1)
