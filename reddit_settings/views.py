from django.shortcuts import render
from django.views.generic import ListView
from .models import Subreddit

class IndexView(ListView):
    model = Subreddit
    template_name = 'reddit_settings/index.html'
