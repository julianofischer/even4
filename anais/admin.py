from django.contrib import admin
from .models import AreaTematica, Modalidade, Evento, Anais, Trabalho,\
    Afiliacao, Autor

admin.site.register(AreaTematica)
admin.site.register(Modalidade)
admin.site.register(Evento)
admin.site.register(Anais)
admin.site.register(Trabalho)
admin.site.register(Afiliacao)
admin.site.register(Autor)
