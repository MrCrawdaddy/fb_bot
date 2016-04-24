from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy

from .models import SubChoice, UserPreferences


class Profile(LoginRequiredMixin, UpdateView):
    model = UserPreferences
    template_name = 'preferences/index.html'
    fields = [
        'sub',
        'time',
    ]
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    success_url = reverse_lazy('account:login')
