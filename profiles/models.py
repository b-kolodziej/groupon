from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in

# Create your models here.
from groupon.stripe_api import secret_key


import stripe

stripe.api_key = secret_key

class UserStripe(models.Model):
	user = models.OneToOneField(User)
	stripe_id = models.CharField(max_length=120, null=True, blank=True)
	phone_number = models.CharField(max_length=120, default=555-777-888)

	def __unicode__(self):
		return self.user.username


def CreateStripeId(sender, user, request, **kwargs):
	new_id, created = UserStripe.objects.get_or_create(user=user)
	if created:
		#add user email to stripe and set stripe id
		stripe_cust = stripe.Customer.create(email=user.email, description=\
								'Customer %s was created' % (user.username))
		print stripe_cust.id
		new_id.stripe_id = stripe_cust.id
		new_id.save()
	else:
		print "stipe has been created"

user_logged_in.connect(CreateStripeId)