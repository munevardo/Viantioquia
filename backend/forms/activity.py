# -*- coding: utf-8 -*-
from django import forms

DEPARTMENTS = (
	('', 'Departamento'),
	('atioquia', 'Antioquia',), 
	('amazonas', 'Amazonas',)
)

TOWNS = (
	('', 'Municipio'),
	('medellin', 'Medellín',),
	('cali', 'Cali',),
	('bogota', 'Bogotá',)
)


class ActivityForm(forms.Form):
	name = forms.CharField(label="Nombre", required=True)
	
	address = forms.CharField(label="Dirección", required=False)
	
	img = forms.ImageField(label="Imagen", required=False)
	
	description = forms.CharField(label="Descripción", required=True, 
		widget=forms.Textarea)
		
	price = forms.IntegerField(label="Precio", required=False)
	
	title = forms.CharField(label="Título", required=False)
	
	department = forms.ChoiceField(label="Departamento", required=True, 
		choices=DEPARTMENTS)
		
	town = forms.ChoiceField(label="Municipio", required=True, 
		choices=TOWNS)
		
	start = forms.DateField(label="Fecha Inicio", required=True,
		widget=forms.DateInput(attrs={}))
	
	end = forms.DateField(label="Fecha Fin", required=True)
