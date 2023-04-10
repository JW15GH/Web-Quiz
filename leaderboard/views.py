from django.shortcuts import render
from django.http import HttpResponse
from .models import Score
from django.template import loader

def leaderboard(request):
    scores = Score.objects.order_by('-score')[:10]
    template = loader.get_template('leaderboard/index.html')
    context = {
        'scores': scores
    }
    return HttpResponse(template.render(context, request))
