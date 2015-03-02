from django.shortcuts import render_to_response, RequestContext, HttpResponseRedirect
from deals.models import Deal



def home(request):
	posts = Deal.objects.get_featured_deals()
	return render_to_response('home.html',
	 						  locals(), 
	 						  context_instance=RequestContext(request))