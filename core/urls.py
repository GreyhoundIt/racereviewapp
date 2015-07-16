
from django.conf.urls import include, url, patterns
import core.views as coreviews

urlpatterns = patterns('',	
	url(r'^$', coreviews.LandingView.as_view()),
	)
