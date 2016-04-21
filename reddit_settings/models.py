from django.db import models
from allauth.socialaccount.models import SocialAccount

class Subreddit(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()

class UserSetting(models.Model):
    subreddit = models.ForeignKey(
        'Subreddit',
        on_delete=models.CASCADE,
    )
    social_account = models.ForeignKey(
        SocialAccount,
        on_delete=models.CASCADE,
    )
    frequency = models.IntegerField()
