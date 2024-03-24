from os import path
from urllib.parse import unquote, urlparse

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand, CommandError

from places.models import Image, Place


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
            self.process_json_url(json_url)
        self.stdout.write(self.style.SUCCESS(
            'Загрузка мест и фотографий завершена.'))

    def process_json_url(self, json_url):
        try:
            response = requests.get(json_url)
            response.raise_for_status()
            place_params = response.json()
        except requests.exceptions.RequestException as err:
            raise CommandError(f"HTTP error occurred: {err}")

        place = self.create_or_update_place(place_params)
        self.load_images_for_place(place, place_params['imgs'])

    def create_or_update_place(self, place_params):
        defaults = {
            'short_description': place_params['description_short'],
            'long_description': place_params['description_long'],
            'latitude': place_params['coordinates']['lat'],
            'longitude': place_params['coordinates']['lng'],
        }
        place, created = Place.objects.get_or_create(
            title=place_params['title'],
            defaults=defaults
        )
        if created:
            self.stdout.write(self.style.SUCCESS(
                f'Успешно добавленно место: {place.title}'))
        else:
            self.stdout.write(self.style.WARNING(
                f'Место уже существует: {place.title}'))
        return place

    def load_images_for_place(self, place, img_urls):
        for img_url in img_urls:
            try:
                response = requests.get(img_url)
                response.raise_for_status()
                filepath = unquote(urlparse(img_url).path)
                filename = path.basename(filepath)
                image_content = ContentFile(response.content, name=filename)
                Image.objects.create(
                    location=place,
                    image=image_content,
                    order=place.images.count() + 1
                )
                self.stdout.write(self.style.SUCCESS(
                    f'Добавлено фото {filename} в место: {place.title}'))
            except requests.exceptions.RequestException as err:
                self.stdout.write(self.style.WARNING(
                    f'Возникла ошибка HTTP при загрузке фотографии: {err}'))
                continue
