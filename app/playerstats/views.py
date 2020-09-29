
# Create your views here.
from django.shortcuts import render

def playerstats(request):
    return render(request, 'playerstats.html', {})
