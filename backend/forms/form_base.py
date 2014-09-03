from django import forms

class FormBase(forms.Form):
	address = forms.CharField()
	img = forms.ImageField()
	description = forms.CharField(required=True)
	price = forms.IntegerField()
	title = forms.CharField()
	#ratings = forms.FloatField(min_value=0, max_value=0)
	department = forms.CharField(required=True)
	town = forms.CharField(required=True)
