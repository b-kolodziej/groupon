from django import forms
from .models import Contact
from django.forms import TextInput, Textarea


class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		widgets = {
			'message': forms.Textarea(attrs={'cols': 50, 'rows': 15})
		}