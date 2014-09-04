from django.http import HttpResponseRedirect
from google.appengine.ext import ndb
from backend.forms.hotel import HotelForm
from django.shortcuts import render


def index(request):
	return render(request, 'hotels/index.html', {
		'form': HotelForm()
	})
	
	
def new(request):

	if request.method == 'GET':
		return render(request, 'hotels/new.html', {
			'form': HotelForm()
		})
		
	else:
		form = HotelForm(request.POST)
		
		if form.is_valid():
			return HttpResponseRedirect('/')
		else
			return render(request, 'hotels/new.html', {
				'form': form
			})
	
