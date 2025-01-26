from django.db import models
from django.conf import settings

# Model pentru Postari (Topicuri)
class Topic(models.Model):
    titlu = models.CharField(max_length=200)  # Titlul postarii
    continut = models.TextField()  # Continutul postarii
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Autorul postarii
    locatie = models.CharField(max_length=255, blank=True, null=True)  # Adresa locatiei (opționala)
    latitudine = models.FloatField(blank=True, null=True)  # Latitudinea locatiei
    longitudine = models.FloatField(blank=True, null=True)  # Longitudinea locatiei
    data_crearii = models.DateTimeField(auto_now_add=True)  # Data crearii

    def __str__(self):
        return self.titlu

# Model pentru Comentarii
class Comentariu(models.Model):
    topic = models.ForeignKey(Topic, related_name='comentarii', on_delete=models.CASCADE)  # Legatura cu topicul
    continut = models.TextField()  # Conținutul comentariului
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Autorul comentariului
    locatie = models.CharField(max_length=255, blank=True, null=True)  # Locatia comentariului (opționala)
    latitudine = models.FloatField(blank=True, null=True)  # Latitudinea locatiei comentariului
    longitudine = models.FloatField(blank=True, null=True)  # Longitudinea locatiei comentariului
    data_crearii = models.DateTimeField(auto_now_add=True)  # Data crearii comentariului

    def __str__(self):
        return f"Comentariu la {self.topic.titlu} de {self.autor.username}"
