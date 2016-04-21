from django.db import models
from django.contrib.auth.models import User


class SubredditPreference(models.Model):
    name = models.CharField(max_length=30)
    url = models.URLField()


class UserSubredditPreference(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE)

    preference = models.ForeignKey(
        SubredditPreference,
        on_delete=models.CASCADE,
    )
