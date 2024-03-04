from os import path
from urllib.parse import urlparse, unquote

import requests
from django.core.management.base import BaseCommand, CommandError
from django.core.files.base import ContentFile
from places.models import Place, Image

class Command(BaseCommand):
    help = 'Загружает локацию из json файла в БД'

    def add_arguments(self, parser):
        parser.add_argument(
            'json_urls',
            nargs='*',
            type=str,
            help='URLs to JSON files'
        )

    def handle(self, *args, **options):
        for json_url in options['json_urls']:
            try:
                response = requests.get(json_url)
                response.raise_for_status()
                place_params = response.json()
            except requests.exceptions.RequestException as err:
                raise CommandError(f"HTTP error occurred: {err}")

            defaults = {
                'description_short': place_params['description_short'],
                'description_long': place_params['description_long'],
                'latitude': place_params['coordinates']['lat'],
                'longitude': place_params['coordinates']['lng'],
            }
            place, created = Place.objects.get_or_create(
                title=place_params['title'],
                defaults=defaults
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created place: {place.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'Place already exists: {place.title}'))

            for img_url in place_params['imgs']:
                try:
                    response = requests.get(img_url)
                    response.raise_for_status()
                    filepath = unquote(urlparse(img_url).path)
                    filename = path.basename(filepath)
                    image_content = ContentFile(response.content, name=filename)
                    image, img_created = Image.objects.get_or_create(
                        location=place,
                        defaults={'image': image_content, 'order': place.images.count() + 1}
                    )
                    if img_created:
                        self.stdout.write(self.style.SUCCESS(f'Added image {filename} to place: {place.title}'))
                except requests.exceptions.RequestException as err:
                    self.stdout.write(self.style.WARNING(f"HTTP error occurred while loading image: {err}"))
                    continue

        self.stdout.write(self.style.SUCCESS('Loading of places and images is complete.'))