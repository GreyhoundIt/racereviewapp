from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
import core.models as coremodels
# Create your views here.

class LandingView(TemplateView):
	template_name = 'base/index.html'

class RaceListView(ListView):
	model = coremodels.Race
	template_name = 'race/list.html'

class RaceDetailView(DetailView):
	model = coremodels.Race
	template_name = 'race/detail.html'
	context_object_name = 'race'

