from django.shortcuts import render

def instrumentos_cuerda(request):
    return render(request, 'vista-instrumentos-cuerda.html')

def instrumentos_percusion(request):
    return render(request, 'vista-instrumentos-percusion.html')

def audio(request):
    return render(request, 'vista-audio.html')


# Create your views here.

