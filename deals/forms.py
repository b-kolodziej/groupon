from django import forms
from .models import Deal

class DealForm(forms.ModelForm):
	class Meta:
		model = Deal
		fields = ('title',
				  'slug', 
				  'description',
				  'publish_date',
				  'expiry_date',
				  'remaining',
				  'price',
				  'deal_price',
				  'featured',
				  'active',)

		widgets = {
			'description': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
		}
