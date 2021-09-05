from django.http.request import HttpRequest
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Saludos Desde la vista de encuestas!")

def detalle(request,pregunta_id):
    return HttpResponse("Estas viendo la pregunta %s." %pregunta_id)

def resultados(reques,pregunta_id):
    response = "Estas vieindo los resultados de la pregunta %s."
    return HttpResponse(response % pregunta_id)

def votar(request,pregunta_id):
    respuesta = "Estas votando por la pregunta " + str(pregunta_id)
    return HttpResponse(respuesta)
