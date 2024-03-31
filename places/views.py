from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from places.models import Place


def show_mainpage(request):
    places = Place.objects.all()
    features = []
    for place in places:
        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.longitude, place.latitude]
            },
            'properties': {
                'title': place.title,
                'placeId': place.id,
                'detailsUrl': reverse('show_place', args=[place.id])
            }
        }
        features.append(feature)

    feature_collection = {
        'type': 'FeatureCollection',
        'features': features
    }
    return render(request, 'places/main_page.html', context={'feature_collection': feature_collection})


def show_place(request, place_id):
    place = get_object_or_404(
        Place.objects.prefetch_related('images'), id=place_id)
    serialized_place = {
        'title': place.title,
        'imgs': [image.image.url for image in place.images.all()],
        'description_short': place.short_description,
        'description_long': place.long_description,
        'coordinates': {
            'lng': place.longitude,
            'lat': place.latitude
        }
    }
    return JsonResponse(serialized_place, safe=False,
                        json_dumps_params={'ensure_ascii': False,
                                           'indent': 4})
