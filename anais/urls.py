from django.urls import path
from .views import home, event_detail, trabalho_detail, home_ajax_search, adicionar_evento

urlpatterns = [
    path('', home, name='home'),
    path('evento/<int:pk>', event_detail),
    path('evento/adicionar', adicionar_evento, name='adicionar_evento'),
    path('evento/<slug:slug>', event_detail, name='eventoslug' ),
    path('evento/<slug:slug_evento>/<slug:slug_trab>/', trabalho_detail, name='trabalho_detail' ),
    path('ajax-search/<str:search_string>', home_ajax_search),
    path('ajax-search/', home_ajax_search)
]
