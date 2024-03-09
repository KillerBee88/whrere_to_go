from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
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
                'detailsUrl': f'/places/{place.id}'
            }
        }
        features.append(feature)

    geo_json = {
        'type': 'FeatureCollection',
        'features': features
    }
    return render(request, 'main_page.html', context={'geo_json': geo_json})


def show_place(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    place_data = {
        'title': place.title,
        'imgs': [image.image.url for image in place.images.all()],
        'description_short': place.short_description,
        'description_long': place.long_description,
        'coordinates': {
            'lng': place.longitude,
            'lat': place.latitude
        }
    }
    return JsonResponse(place_data, safe=False,
                        json_dumps_params={'ensure_ascii': False,
                                           'indent': 4})
