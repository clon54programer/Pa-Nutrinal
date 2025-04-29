from django.shortcuts import render
from django.http import HttpResponse,Http404

# Create your views here.

def index(request):
    return HttpResponse("Bienvenido a nutrinal")


def login(request,type_user: str):

    if type_user == "admin":
        return HttpResponse(f"Bienvenido: {type_user}")
    elif type_user == "client":
        return HttpResponse(f"Bienvenido: {type_user}")
    elif type_user == "seller":
        return HttpResponse(f"Bienvenido: {type_user}")
    #else:
    #    raise Http404("El tipo de usuario es invalido")


    raise Http404("El tipo de usuario es invalido")