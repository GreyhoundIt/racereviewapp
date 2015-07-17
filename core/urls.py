
from django.conf.urls import include, url, patterns
import core.views as coreviews

urlpatterns = patterns('',	
	url(r'^$', coreviews.LandingView.as_view()),
	url(r'race/$', coreviews.RaceListView.as_view()),
	url(r'race/(?P<pk>\d+)/detail/$', coreviews.RaceDetailView.as_view(), name='race_list'),
	url(r'race/create/$', coreviews.RaceCreateView.as_view()),
	url(r'search/$', coreviews.SearchRaceListView.as_view()),
	url(r'race/(?P<pk>\d+)/update/$', coreviews.RaceUpdateView.as_view(), name='race_update'),
	url(r'race/(?P<pk>\d+)/review/create/$', coreviews.ReviewCreateView.as_view(), name='review_create'),
	url(r'race/(?P<pk>\d+)/review/update/$', coreviews.ReviewUpdateView.as_view(), name='review_update'),
	)	
