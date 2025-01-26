from django.contrib import admin
from .models import Eveniment

@admin.register(Eveniment)
class EvenimentAdmin(admin.ModelAdmin):
    list_display = ('titlu', 'data_eveniment', 'locatie')  # Coloane vizibile in lista din admin
    search_fields = ('titlu', 'locatie')  # Cautare dupa titlu sau locatie
    list_filter = ('data_eveniment',)  # Filtru după data
