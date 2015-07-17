
from django.conf.urls import include, url, patterns
import core.views as coreviews

urlpatterns = patterns('',	
	url(r'^$', coreviews.LandingView.as_view()),
	url(r'race/$', coreviews.RaceListView.as_view()),
	url(r'race/(?P<pk>\d+)/detail/$', coreviews.RaceDetailView.as_view(), name='race_list'),
	)	
