from django.http import HttpResponseRedirect
from google.appengine.ext import ndb
from django.shortcuts import render
from backend.forms.hotel import HotelForm
from backend.models import HotelModel, TownModel, DepartmentModel


def hotels(request):
	return hotels_page(request, 1)
	
	
	
################################################################



def hotels_page(request, page):
	if request.method == 'POST':
		r = {'next': page+1, 'prev': page-1, 'post': request.POST.get('text')}
	else:
		r = {'next': page+1, 'prev': page-1}	
	return render(request, 'hotels/list_hotels.html', r)
	
	
	
################################################################	




def new(request):

	if request.method == 'GET':
		return render(request, 'hotels/new.html', {
			'form': HotelForm()
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
