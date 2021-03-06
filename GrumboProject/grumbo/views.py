from django.shortcuts import render
from django.views.generic import (View, TemplateView,)
# Create your views here.

class IndexView(TemplateView):
    template_name = 'grumbo/index.html'

class GuideView(TemplateView):
    template_name = 'grumbo/guide.html'

class CommandsView(TemplateView):
    template_name = 'grumbo/commands.html'

class ClassesView(TemplateView):
    template_name = 'grumbo/classes.html'

class StatsView(TemplateView):
    template_name = 'grumbo/stats.html'

class AboutView(TemplateView):
        template_name = 'grumbo/about.html'

class BossView(TemplateView):
        template_name = 'grumbo/boss.html'
