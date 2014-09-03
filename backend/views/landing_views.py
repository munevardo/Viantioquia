from django.http import HttpResponseRedirect
from google.appengine.ext import ndb
from backend.forms.hotel import HotelForm
from django.shortcuts import render


def index(request):
	return render(request, 'landings/index.html')


def jardin(request):
	return render(request, 'landings/jardin.html')


def andes(request):
	return render(request, 'landings/andes.html')


def hispania(request):
	return render(request, 'landings/hispania.html')