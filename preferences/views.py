from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse, reverse_lazy

from .models import SubChoice, UserPreferences


class Profile(LoginRequiredMixin, DetailView):
    model = UserPreferences
    template_name = 'preferences/index.html'
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'

def update_subreddits(request, pk):
    userpreferences = get_object_or_404(UserPreferences, pk=pk)
    try:
        userpreferences.sub.add(request.POST['sub'])
        userpreferences.save()
    except(KeyError, UserPreferences.DoesNotExist):
        return render(request, 'preferences/index.html', {
            'userpreferences': userpreferences,
            'error_message': str(KeyError),
        })
    else:
        return HttpResponseRedirect(reverse_lazy('profile:profile',
            args=[userpreferences.id]))

def update_time(request, pk):
    userpreferences = get_object_or_404(UserPreferences, pk=pk)
    try:
        userpreferences.time = request.POST['time']
        userpreferences.save()
    except (KeyError, UserPreferences.DoesNotExist):
        return render(request, 'preferences/index.html', {
            'userpreferences': userpreferences,
            'error_message': str(KeyError),
        })
    else:
        return HttpResponseRedirect(reverse_lazy('profile:profile',
            args=[userpreferences.id]))
