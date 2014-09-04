from django.http import HttpResponseRedirect
from google.appengine.ext import ndb
from django.shortcuts import render
from backend.forms.hotel import HotelForm
from backend.models import HotelModel, TownModel, DepartmentModel


def hotels(request):
	return render(request, 'hotels/list_hotels.html', {
		'hotels': HotelModel.query().fetch()
	})
	
	
def new(request):

	if request.method == 'GET':
		return render(request, 'hotels/new.html', {
			'form': HotelForm(),
			'form_url': '/nuevo/'
		})
		
	else:
		form = HotelForm(request.POST)
		
		if form.is_valid():
		
			hotel = HotelModel(
				name = form.cleaned_data['name'],
				address = form.cleaned_data['address'],
				description = form.cleaned_data['description'],
				title = form.cleaned_data['title'],
				price = form.cleaned_data['price']
			)			
			
			
			hotel.put()
		
			return HttpResponseRedirect('/')
			
		else:
			return render(request, 'hotels/new.html', {
				'form': form
			})

