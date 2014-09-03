from django import forms

class ActivityForm(forms.Form):
	name = forms.CharField()
	address = forms.CharField()
	img = forms.ImageField()
	description = forms.CharField()
	price = forms.IntegerField()
	title = forms.CharField()
	ratings = forms.FloatField()
	department = forms.CharField()
	town = forms.CharField()
	start = forms.DateField()
	end = forms.DateField()
