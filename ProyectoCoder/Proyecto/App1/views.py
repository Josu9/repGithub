from django.shortcuts import render
 

def inicio (request):
     
    return render(request, "App1/inicio.html")

def bibliotecas(request):
     
    return render(request, "App1/bibliotecas.html")