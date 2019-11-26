from .models import Destination


def filtered_destinations(request):
    filtered_destinations = Destination.objects.order_by('views')[0:3]
    return {'filtered_destinations': filtered_destinations}