from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Congreso, Persona

class IndexView(generic.ListView):
    template_name = 'listas/index.html'
    context_object_name = 'latest_congreso_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Congreso.objects.order_by('-fecha')[:5]

class CongresoList(generic.ListView):
    model = Congreso
    template_name = 'listas/congreso_list.html'
    
class PersonaList(generic.ListView):
    model = Persona
    template_name = 'listas/persona_list.html'

class CongresoDetail(generic.DetailView):
    model = Congreso
    template_name = 'listas/congreso_detail.html'

class PersonaDetail(generic.DetailView):
    model = Persona
    template_name = 'listas/persona_detail.html'
