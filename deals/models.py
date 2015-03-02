from django.db import models

# Create your models here.
class DealManager(models.Manager):
	def get_featured_deals(self):
		return super(DealManager, self).filter(featured=True)


class Deal(models.Model):
	title = models.CharField(max_length=120)
	slug = models.SlugField()
	description = models.CharField(max_length=5000, null=True, blank=True)
	publish_date = models.DateTimeField(auto_now=False,
									    auto_now_add=False,
									    null=True,
									    blank=True)
	expiry_date = models.DateTimeField(auto_now=False,
									   auto_now_add=False,
									   null=True,
									   blank=True)
	remaining = models.IntegerField(null=True, blank=True)
	price = models.DecimalField(decimal_places=2, max_digits=50)
	deal_price = models.DecimalField(decimal_places=2, max_digits=50)
	featured = models.BooleanField(default=False)
	active = models.BooleanField(default=True)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	objects = DealManager()

	def __unicode__(self):
		return self.title