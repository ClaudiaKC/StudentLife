from django.urls import path
from .views import lista_topicuri, detalii_topic, harta_globala, adauga_topic

urlpatterns = [
    path('', lista_topicuri, name='lista_topicuri'),
    path('<int:topic_id>/', detalii_topic, name='detalii_topic'),
    path('adauga/', adauga_topic, name='adauga_topic'),  # URL pentru adaugarea unei postari
    path('harta/', harta_globala, name='harta_globala'),
]
