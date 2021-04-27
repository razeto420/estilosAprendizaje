from django.shortcuts import render, HttpResponse

def cuestionario(request):
    return render(request,"ProyectoWebApp/cuestionario.html")

# Create your views here.
