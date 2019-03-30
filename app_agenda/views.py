from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.

from .models import *

class HomePageView(ListView):
    model=Agenda
    template_name='app_agenda/home.html'