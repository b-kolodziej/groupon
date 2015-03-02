from django.contrib import admin
from .models import UserStripe
# Register your models here.

class UserStripeAdmin(admin.ModelAdmin):
	class Meta:
		model = UserStripe


admin.site.register(UserStripe, UserStripeAdmin)