from django.contrib import admin
from .models import Subreddit, UserSetting


admin.site.register(Subreddit)
admin.site.register(UserSetting)
