from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Evento, Trabalho
from django.http import JsonResponse, HttpResponse
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder

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
    print('####slug####')
    if slug is not None:
        print('####slug 2####')
        evento = get_object_or_404(Evento, slug=slug)
        print(evento)
    else:
        evento = get_object_or_404(Evento, pk=pk)

    edicoes_anteriores = []
    e = evento
    while e.edicao_anterior is not None:
        e = e.edicao_anterior
        edicoes_anteriores.append(e)

    return render(request, 'anais/event_detail.html', {'evento':evento, 'edicoes_anteriores':edicoes_anteriores})

def home_ajax_search(request, search_string):
    eventos = Evento.objects.filter(titulo__icontains=search_string)
    serialized = serializers.serialize('json', eventos, cls=DjangoJSONEncoder)
    return HttpResponse(serialized, content_type='application/json')


def trabalho_detail(request, slug_trab, slug_evento):
    evento = get_object_or_404(Evento, slug=slug_evento)
    trabalho = get_object_or_404(Trabalho, slug=slug_trab)
    return render(request, 'anais/trabalho_detail.html', {'evento':evento, 'trabalho':trabalho})
