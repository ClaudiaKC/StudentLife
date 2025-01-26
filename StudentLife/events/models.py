from django.db import models

class Eveniment(models.Model):
    titlu = models.CharField(max_length=200)  # Titlul evenimentului
    descriere = models.TextField()  # Descrierea evenimentului
    locatie = models.CharField(max_length=255)  # Locatia
    data_eveniment = models.DateField()  # Data evenimentului
    imagine = models.ImageField(upload_to='event_images/', blank=True, null=True)  # Imaginea asociata

    def __str__(self):
        return self.titlu
