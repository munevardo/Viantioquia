from django import forms

class ContactForm(forms.Form):

	name = forms.CharField(label="Nombre", required=True, 
		widget=forms.TextInput(
			attrs={
				'placeholder': 'Nombre'
			}))
		
	email = forms.EmailField(label="Email", required=True, 
		widget = forms.TextInput(
			attrs={
				'placeholder': 'email'
			}))
		
	message = forms.CharField(label="Mensaje", required=True, 
		widget = forms.Textarea(
			attrs={
				'placeholder': 'Mensaje'
			}))
