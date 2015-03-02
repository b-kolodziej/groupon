from django.contrib import admin

# Register your models here.
from .forms import DealForm
from .models import Deal

class DealAdmin(admin.ModelAdmin):
	class Meta:
		model = Deal

admin.site.register(Deal, DealAdmin)