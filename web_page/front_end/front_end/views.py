from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

def search(request):
    tweets = []
    words_requested = request.GET["tweet"]
    tweets.append(words_requested)
    return render(request, 'search.html', {"Tweets" : tweets})