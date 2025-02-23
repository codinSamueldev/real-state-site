from django.shortcuts import render
from django.db.models import Q

from landing.models import Properties

# Create your views here.
def properties_listing(request):
    query = Q()

    country = request.GET.get('country', None)
    city = request.GET.get('city', None)
    property_type = request.GET.get('property_type', None)
    min_price = request.GET.get('min_price', None)
    max_price = request.GET.get('max_price', None)
    
    if country:
        query &= Q(country__icontains=country)

    if city:
        query &= Q(city__icontains=city)

    if property_type:
        query &= Q(property_type__icontains=property_type)
    
    if min_price:
        query &= Q(price__gte=float(min_price))
    
    if max_price:
        query &= Q(price__lte=float(max_price))

    
    if query.children:
        properties = Properties.objects.filter(query)
    else:
        properties = Properties.objects.all()

    
    countries = Properties.objects.order_by().values('country').distinct()


    context = {
        'properties': properties,
        'countries': countries,
        'filters': {
            'country': country,
            'city': city,
            'property_type': property_type,
            'min_price': min_price,
            'max_price': max_price
        }
    }

    return render(request, 'listing/listing.html', context)


