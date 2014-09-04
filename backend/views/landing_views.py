from django.http import HttpResponseRedirect
from google.appengine.ext import ndb
from django.shortcuts import render
# Import Forms
from backend.forms.hotel import HotelForm
from backend.forms.activity import ActivityForm


def index(request):
	return render(request, 'landings/index.html')


def jardin(request):
	return render(request, 'landings/jardin.html')


def andes(request):
	return render(request, 'landings/andes.html')


def hispania(request):
	return render(request, 'landings/hispania.html')
	
	
def test(request):
	if request.method == 'GET':
		form = ActivityForm()
	else:
		form = ActivityForm(request.POST)
	
	if form.is_valid():
		return render(request, 'test.html', {
			'form': ActivityForm(),
			'msg': 'Form send OK!'
		})
	else:
		return render(request, 'test.html', {
			'form': form
		})
