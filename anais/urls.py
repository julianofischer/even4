from django.urls import path
from .views import home, event_detail

urlpatterns = [
    path('', home, name='home'),
    path('evento/<int:pk>', event_detail),
    path('evento/<str:slug>', event_detail ),
]
