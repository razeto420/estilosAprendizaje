from django.shortcuts import render, HttpResponse

def Home(request):
    return render(request,"cuestionario/home.html")

# Create your views here.

def Pregunta(request):
    return render(request,"cuestionario/pregunta.html")


