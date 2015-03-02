from django.shortcuts import render, render_to_response, HttpResponseRedirect, RequestContext

from .forms import ContactForm
# Create your views here.


def contact(request):

	form = ContactForm(request.POST or None)

	if form.is_valid():
		save_form = form.save(commit=False)
		save_form.save()

	return render_to_response('form.html',
							  locals(), 
							  context_instance=RequestContext(request))