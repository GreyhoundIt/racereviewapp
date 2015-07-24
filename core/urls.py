
from django.conf.urls import include, url, patterns
from django.contrib.auth.decorators import login_required
import core.views as coreviews

urlpatterns = patterns('',	
	url(r'^$', coreviews.RaceListView.as_view()),
	url(r'^about/$', coreviews.LandingView.as_view()),
	url(r'race/$', coreviews.RaceListView.as_view()),
	url(r'race/(?P<pk>\d+)/detail/$', coreviews.RaceDetailView.as_view(), name='race_list'),
	url(r'race/create/$', login_required(coreviews.RaceCreateView.as_view())),
	url(r'search/$', coreviews.SearchRaceListView.as_view()),
	url(r'race/(?P<pk>\d+)/update/$', login_required(coreviews.RaceUpdateView.as_view()), name='race_update'),
	url(r'race/(?P<pk>\d+)/review/create/$', login_required(coreviews.ReviewCreateView.as_view()), name='review_create'),
	url(r'race/(?P<pk>\d+)/review/update/$', login_required(coreviews.ReviewUpdateView.as_view()), name='review_update'),
	url(r'entrance/$', coreviews.entrance),
	)	
