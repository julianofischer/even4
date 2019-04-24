from django.shortcuts import render

# Create your views here.
# home (eventos)
# evento (details)
# trabalhos (trabalhos details)
def home(request):
    return render(request, 'anais/home.html')
