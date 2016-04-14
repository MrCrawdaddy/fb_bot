from django.db import models


class RedditSetting(models.Model):
    url = models.URLField()
