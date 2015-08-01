from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from sitegate.decorators import redirect_signedin, sitegate_view, signup_view, signin_view
from sitegate.signup_flows.classic import SimpleClassicSignup, ClassicWithEmailSignup
from sitegate.signin_flows.classic import ClassicSignin
import core.models as coremodels
# Create your views here.

class LandingView(TemplateView):
	template_name = 'base/index.html'

class RaceListView(ListView):
	model = coremodels.Race
	template_name = 'race/list.html'
	paginate_by = 5

class SearchRaceListView(RaceListView):

	def get_queryset(self):
		incoming_data = self.request.GET.get('query', '')
		return coremodels.Race.objects.filter(title__icontains=incoming_data)

class SearchRaceDistanceListView(RaceListView):

	def get_queryset(self):
		incoming_data = self.request.GET.get('query', '')
		return coremodels.Race.objects.filter(distance__icontains=incoming_data)


class RaceDetailView(DetailView):
	model = coremodels.Race
	template_name = 'race/detail.html'
	context_object_name = 'race'
	

	def get_context_data(self, **kwargs):
		context = super(RaceDetailView, self).get_context_data(**kwargs)
		race = coremodels.Race.objects.get(id=self.kwargs['pk'])
		if self.request.user.is_authenticated():
			user_reviews =coremodels.Review.objects.filter(race=race, user=self.request.user)
			if user_reviews.count() > 0:
				context['user_review'] = user_reviews[0]
			else:
				context['user_review'] = None

		return context 
	
class RaceCreateView(CreateView):
	model = coremodels.Race
	template_name = 'base/form.html'
	fields = "__all__"

class RaceUpdateView(UpdateView):
	model = coremodels.Race
	template_name = 'base/form.html'
	fields = "__all__"

class ReviewCreateView(CreateView):
	model = coremodels.Review
	template_name = 'base/form.html'
	fields = ['review', 'valueformoney', 'atmosphere', 'goodybag' ,'rating']

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.instance.race = coremodels.Race.objects.get(id=self.kwargs['pk'])
		return super(ReviewCreateView, self).form_valid(form)

	def get_success_url(self):
		return self.object.race.get_absolute_url()

class ReviewUpdateView(UpdateView):
	model = coremodels.Review
	template_name = 'base/form.html'
	fields = ['review', 'valueformoney', 'atmosphere', 'goodybag' ,'rating']

	def get_object(self):
		return coremodels.Review.objects.get(race__id=self.kwargs['pk'], user=self.request.user)

	def get_success_url(self):
		return self.object.race.get_absolute_url()



@signup_view(widget_attrs={'class': 'form-control', 'placeholder': lambda f: f.label}, template='form_bootstrap3', flow=ClassicWithEmailSignup)
@signin_view(widget_attrs={'class': 'form-control', 'placeholder': lambda f: f.label}, template='form_bootstrap3', flow=ClassicSignin)
@redirect_signedin('race')
def entrance(request):
    return render(request, 'base/entrance.html', {'title': 'Sign in & Sign up'})

