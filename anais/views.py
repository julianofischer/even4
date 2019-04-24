from django.shortcuts import render
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
