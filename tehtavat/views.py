from django.http import (
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseNotFound,
)
from django.shortcuts import render

from .models import Tehtava


def etusivu(request):
    tiedot = {
        "tehtavat": Tehtava.objects.all(),
    }
    response = render(request, "etusivu.html", context=tiedot)
    return response


def tehtava_sivu(request, id):
    try:
        tehtava = Tehtava.objects.get(id=id)
    except Tehtava.DoesNotExist:
        return HttpResponseNotFound(f"Tehtävää {id} ei löydy.")

    if request.method == "POST":
        toiminto = request.POST.get("toiminto")
        if toiminto == "merkitse_tehdyksi":
            tehtava.tehty = True
            tehtava.save()
        else:
            return HttpResponseBadRequest("Tuntematon toiminto")

    return render(request, "tehtava.html", context={"tehtava": tehtava})


def tietoa(request):
    response = render(request, "tietoa.html")
    return response

def yhteystiedot(request):
    return HttpResponse("<html><body><h1>Yhteystiedot</h1></body></html>")
