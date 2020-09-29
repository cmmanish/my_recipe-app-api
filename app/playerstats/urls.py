from django.urls import path
from playerstats import views

urlpatterns = [
    path('', views.playerstats, name='playerstats'),
]
