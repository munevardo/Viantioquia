from django import forms
from django.forms import widgets

class HotelForm(forms.Form):
	address = forms.CharField()
	img = forms.ImageField()
	description = forms.CharField(required=True)
	price = forms.IntegerField()
	title = forms.CharField()
	ratings = forms.FloatField(min_value=0, max_value=5, 
		widget = forms.HiddenInput())
	department = forms.CharField(required=True)
	town = forms.CharField(required=True)
