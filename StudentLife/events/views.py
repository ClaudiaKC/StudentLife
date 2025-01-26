from django.shortcuts import render
from .models import Eveniment

def lista_evenimente(request):
    evenimente = Eveniment.objects.all().order_by('-data_eveniment')  # Cele mai recente evenimente
    return render(request, 'events/lista_evenimente.html', {'evenimente': evenimente})
