from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.auth import models as auth_model
from preferences.models import UserPreferences

class MyAccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        path = "/profile/{id}"
        if len(UserPreferences.objects.filter(user__id=request.user.id)) is 0:
            new_user = UserPreferences(user=request.user)
            new_user.save()
        user_preferences = UserPreferences.objects.filter(user__id=request.user.id)
        print(str(user_preferences))
        return path.format(id=user_preferences[0].id)
