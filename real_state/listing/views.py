from django.shortcuts import render

from landing.models import Properties

# Create your views here.
def properties_listing(request):
    return render(request, 'listing/listing.html', {'properties': Properties.objects.all()})


