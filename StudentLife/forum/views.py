from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic, Comentariu
from .forms import TopicForm


# View pentru listarea tuturor postarilor
def lista_topicuri(request):
    topicuri = Topic.objects.all().order_by('-data_crearii')  # Cele mai recente postari
    return render(request, 'forum/lista_topicuri.html', {'topicuri': topicuri})


# View pentru detaliile unei postari
def detalii_topic(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    comentarii = topic.comentarii.all()  # Comentariile asociate postarii

    if request.method == 'POST':
        continut = request.POST.get('continut')
        locatie = request.POST.get('locatie', '')
        latitudine = request.POST.get('latitudine')
        longitudine = request.POST.get('longitudine')

        # salvam comentariul doar daca exists continut si utilizatorul este autentificat
        if continut and request.user.is_authenticated:
            Comentariu.objects.create(
                topic=topic,
                autor=request.user,
                continut=continut,
                locatie=locatie,
                latitudine=latitudine,
                longitudine=longitudine,
            )

        return redirect('detalii_topic', topic_id=topic_id)  # Reincarca pagina

    return render(request, 'forum/detalii_topic.html', {
        'topic': topic,
        'comentarii': comentarii,  # Comentariile trimise catre sablon
    })



# View pentru afisarea hartii globale
def harta_globala(request):
    topicuri = Topic.objects.exclude(latitudine__isnull=True, longitudine__isnull=True)
    # Pregatim datele locatiilor pentru harta Google
    topicuri_json = [
        {
            "titlu": topic.titlu,
            "locatie": topic.locatie,
            "latitudine": topic.latitudine,
            "longitudine": topic.longitudine,
        }
        for topic in topicuri
    ]
    return render(request, 'forum/harta.html', {
        'topicuri': topicuri_json,
        'GOOGLE_MAPS_API_KEY': "AIzaSyDL9Wp5goX8nTk44pZ5uwo_cMAcCbC1ax0",
    })


# View pentru adaugarea unui topic nou
def adauga_topic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            # Cream un obiect din formular, dar nu îl salvam imediat
            topic = form.save(commit=False)
            # Setam utilizatorul conectat ca autor
            topic.autor = request.user
            # Salvam obiectul in baza de date
            topic.save()
            return redirect('lista_topicuri')  # Redirectioneaza la lista topicurilor
    else:
        form = TopicForm()
    return render(request, 'forum/adauga_topic.html', {'form': form})
