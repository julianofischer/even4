from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Evento

# Create your views here.
# home (eventos)
# evento (details)
# trabalhos (trabalhos details)
def home(request):
    eventos = Evento.objects.all()
    paginator = Paginator(eventos, 9)
    page = request.GET.get('page')
    eventos = paginator.get_page(page)
    return render(request, 'anais/home.html', {'eventos':eventos})

def event_detail(request, slug=None, pk=None):
    evento = None
    if slug is not None:
        evento = get_object_or_404(Evento, slug=slug)
    else:
        evento = get_object_or_404(Evento, pk=pk)

    return render(request, 'anais/event_detail.html', {'evento':evento})
