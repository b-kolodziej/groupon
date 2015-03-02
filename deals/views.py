from django.shortcuts import render, Http404

from .models import Deal

# Create your views here.
def deal_detail(request, year, month, slug):
	try:
		post = Deal.objects.filter(publish_date__year=year).\
									filter(publish_date__month=month).\
									get(slug=slug)
	except Deal.MultipleObjectsReturned:
		post = Deal.objects.filter(slug=slug)[0]
	except:
		raise Http404

	context = {
		'year' : year,
		'month' : month,
		'slug' : slug,
		'post' : post,
	}

	return render(request, 'deals/deal_detail.html', context)