from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
from console import Console
#import sys
#sys.path.append('/Users/alejandrotero/Documents/UTEC/Ciclo 6/BD2/Proyecto2_Hito1_BD2')

def search(request):
    tweets = request.GET["tweet"]
    dic = Console()
    answer = dic.print_in_console(tweets)
    return render(request, 'search.html', {"Tweets": answer})