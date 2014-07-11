from django.shortcuts import render_to_response
from kannada.models import Movie
from kannada.forms import MovieForm
from django.template.context import RequestContext
import json
from django.http import HttpResponse

def search(request):
	movies = Movie.objects.all()
	movie_names = []
	for movie in movies:
		movie_names.append(str(movie.name))
	if request.method == 'POST':
		form = MovieForm(request.POST)
		print form.is_valid()
		if form.is_valid():
			print form.is_valid()
			movie_name = form.cleaned_data['movie_name']
			print movie_name
			movie_description = Movie.objects.get(name = movie_name)
			print movie_description.tagline
			form = MovieForm()
			print "inside post"
			return render_to_response('index.html',locals(),context_instance=RequestContext(request))
	else:
		movies = Movie.objects.all()
		movie_names = []
		for movie in movies:
			movie_names.append(str(movie.name))
			form = MovieForm(request.GET)
			if form.is_valid():
				movie_name = form.cleaned_data['movie_name']
				movie_description = Movie.objects.get(name = movie_name)
				print movie_description.tagline
				print "outside post"
				form = MovieForm()
	return render_to_response('index.html',locals(),context_instance=RequestContext(request))


def search_autocomplete(request):
	movie_data = []
	if request.GET.has_key(u'term'):
		value = request.GET[u'term']
		if len(value) > 1:
			movies = Movie.objects.filter(name__icontains=value)
			for movie in movies:
				movie_data.append(dict([('label', movie.name), ('value', movie.name)]))
	print movie_data
	jso = json.dumps([movie for movie in movie_data])
	print json
	return HttpResponse(jso, mimetype = 'application/json')

def test(request):
	return render_to_response('test.html')

