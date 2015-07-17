from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
import core.models as coremodels
# Create your views here.

class LandingView(TemplateView):
	template_name = 'base/index.html'

class RaceListView(ListView):
	model = coremodels.Race
	template_name = 'race/list.html'

class SearchRaceListView(RaceListView):

	def get_queryset(self):
		incoming_data = self.request.GET.get('query', '')
		return coremodels.Race.objects.filter(title__icontains=incoming_data)

class RaceDetailView(DetailView):
	model = coremodels.Race
	template_name = 'race/detail.html'
	context_object_name = 'race'
	
class RaceCreateView(CreateView):
	model = coremodels.Race
	template_name = 'base/form.html'
	fields = "__all__"

