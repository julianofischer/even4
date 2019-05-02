from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from .models import Evento, Trabalho, AreaTematica, Anais
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

from django.utils.timezone import get_current_timezone
from datetime import datetime
from django.db import transaction

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

def home_ajax_search(request, search_string=None):
    if search_string is None:
        eventos = Evento.objects.all()
    else:
        eventos = Evento.objects.filter(titulo__icontains=search_string)
    paginator = Paginator(eventos, 9)
    page = request.GET.get('page')
    eventos = paginator.get_page(page)
    return render(request, 'anais/home/eventos.html', {'eventos':eventos})


def trabalho_detail(request, slug_trab, slug_evento):
    evento = get_object_or_404(Evento, slug=slug_evento)
    trabalho = get_object_or_404(Trabalho, slug=slug_trab)
    return render(request, 'anais/trabalho_detail.html', {'evento':evento, 'trabalho':trabalho})

def __save_event(request):
    evento_titulo = request.POST['titulo-evento']
    evento_local = request.POST['local-evento']
    evento_apresentacao = request.POST['apresentacao-evento']
    evento_comissao_org = request.POST['comissao-organizadora-evento']
    evento_comissao_cie = request.POST['comissao-cientifica-evento']
    evento_areas_tematicas = request.POST['areas-tematicas']
    evento_contato = request.POST['contato-evento']
    evento_ev_anterior = int(request.POST['evento-anterior'])

    evento = Evento()
    evento.titulo = evento_titulo
    evento.local = evento_local
    evento.apresentação = evento_apresentacao
    evento.comissao_organizadora = evento_comissao_org
    evento.comissao_cientifica = evento_comissao_cie
    evento.contato = evento_contato

    icone = request.FILES['file-icone']
    banner = request.FILES['file-banner']
    fs = FileSystemStorage()
    evento.icone = fs.save(icone.name, icone)
    evento.banner = fs.save(banner.name, banner)

    evento.save()
    for area_id in evento_areas_tematicas:
        area_id = int(area_id)
        evento.areas_tematicas.add(AreaTematica.objects.get(pk=area_id))

    evento_anterior = Evento.objects.get(pk=evento_ev_anterior)
    evento.edicao_anterior = evento_anterior
    evento.save()
    return evento

def __save_anais(request, commit=True):
    titulo = request.POST['titulo-anais']
    isbn = request.POST['isbn-anais']
    data_de_publicacao = request.POST['data-anais']
    pais_de_publicacao = request.POST['idioma-anais']
    idioma_de_publicacao = request.POST['pais-anais']
    anais = Anais()
    anais.titulo = titulo
    anais.isbn = isbn
    anais.idioma_de_publicacao = idioma_de_publicacao
    anais.pais_de_publicacao = pais_de_publicacao
    tz = get_current_timezone()
    dt = tz.localize(datetime.strptime(data_de_publicacao, '%Y-%m-%d'))
    anais.data_de_publicacao = dt
    anais.save()
    return anais

def adicionar_evento(request):
    saved = False
    print(request.FILES)
    if request.method == 'POST':
        with transaction.atomic():
            evento = __save_event(request)
            evento.anais = __save_anais(request)
            evento.save()
            saved = True

    eventos = Evento.objects.all()
    areas_tematicas = AreaTematica.objects.all()
    contexto = {'eventos':eventos, 'areas_tematicas':areas_tematicas, 'saved':saved}
    return render(request, 'anais/create_event.html', contexto)

from .forms import AnaisForm, EventoForm
def adicionar_modelform(request):
    if request.method == 'POST':
        anais_form = AnaisForm(request.POST)
        evento_form = EventoForm(request.POST, request.FILES)
        if anais_form.is_valid() and evento_form.is_valid():
            anais_model = anais_form.save(commit=False)
            evento_model = evento_form.save(commit=False)
            anais_model.save()
            evento_model.anais = anais_model
            evento_model.save()
            return redirect('/')
        else:
            context = {'anais_form':anais_form, 'evento_form':evento_form}
            return render(request, 'anais/adicionar_modelform.html', context)
    else:
        anais_form = AnaisForm()
        evento_form = EventoForm()
        context = {'anais_form':anais_form, 'evento_form':evento_form}
        return render(request, 'anais/adicionar_modelform.html', context)

def adicionar_modelform(request):
    if request.method == 'POST':
        anais_form = AnaisForm(request.POST)
        evento_form = EventoForm(request.POST, request.FILES)
        if anais_form.is_valid() and evento_form.is_valid():
            anais_model = anais_form.save(commit=False)
            evento_model = evento_form.save(commit=False)
            anais_model.save()
            evento_model.anais = anais_model
            evento_model.save()
            return redirect('/')
        else:
            context = {'anais_form':anais_form, 'evento_form':evento_form}
            return render(request, 'anais/adicionar_modelform2.html', context)
    else:
        anais_form = AnaisForm()
        evento_form = EventoForm()
        context = {'anais_form':anais_form, 'evento_form':evento_form}
        return render(request, 'anais/adicionar_modelform2.html', context)
