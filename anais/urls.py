from django.urls import path
from .views import home, event_detail, trabalho_detail, home_ajax_search

urlpatterns = [
    path('', home, name='home'),
    path('evento/<int:pk>', event_detail),
    path('evento/<str:slug>', event_detail, name='eventoslug' ),
    path('trabalhos/<str:slug_evento>/<str:slug_trab>/', trabalho_detail, name='trabalho_detail' ),
    path('ajax-search/<str:search_string>', home_ajax_search),
    path('ajax-search/', home_ajax_search)
]
