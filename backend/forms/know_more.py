from django import forms

class KnowMoreForm(forms.Form):
	email = forms.EmailField(label="email", required=True, 
		widget=forms.TextInput(attrs={'placeholder': 'email'}))
