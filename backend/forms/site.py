from django import forms

class SiteForm(forms.Form):
	address = forms.CharField(requied=False)
	img = forms.ImageField(required=False)
	description = forms.CharField(required=True)
	title = forms.CharField(required=False)
	ratings = forms.FloatField(required=False, default=0.0)
	department = forms.ChoiceField(required=True)
	town = forms.ChoiceField(required=True)
