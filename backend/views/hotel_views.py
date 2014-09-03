from django.http import HttpResponseRedirect
from google.appengine.ext import ndb
from backend.forms.hotel import HotelForm
from django.shortcuts import render


def index(request):
	return render(request, 'hotels/index.html', {
		'form': HotelForm()
	})
