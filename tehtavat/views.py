from django.http import HttpResponse
from django.shortcuts import render

from .models import Tehtava


def etusivu(request):
    tiedot = {
        "tehtavat": Tehtava.objects.all(),
    }
    response = render(request, "etusivu.html", context=tiedot)
    return response

def tietoa(request):
    response = render(request, "tietoa.html")
    return response

def yhteystiedot(request):
    return HttpResponse("<html><body><h1>Yhteystiedot</h1></body></html>")
