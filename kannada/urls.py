from django.conf.urls import patterns, url
from kannada import views

urlpatterns = patterns('',
    url(r'^$', views.search, name='search'),
	url(r'^test/$', views.test, name='test'),
	url(r'^search_autocomplete/$', views.search_autocomplete, name='auto')
	
	
)


