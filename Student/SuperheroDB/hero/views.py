from django.shortcuts import render

# Create your views here.
from pathlib import Path
from django.views.generic import TemplateView
from .models import Superhero


def photo_list():
    def photo_details(i, f):

        caption = f'Caption for Photo {i}'
        return dict(id=i, file=f, caption=caption)

    photos = Path('static/images').iterdir()
    photos = [photo_details(i, f) for i, f in enumerate(photos)]
    return photos


class PhotoListView(TemplateView):
    template_name = 'photos.html'

    def get_context_data(self, **kwargs):
        return dict(photos=photo_list())


class PhotoDetailView(TemplateView):
    template_name = 'photo.html'

    def get_context_data(self, **kwargs):
        i = kwargs['id']
        photos = photo_list()
        p = photos[i]
        return dict(photo=p)


class SpidermanView(TemplateView):
    template_name = "phototest.html"

    def get_context_data(self, **kwargs):
        return {
            'title': 'Spiderman',
            'image': '/static/images/spiderman1610.jpg',
            'strength1': 'Super Strength',
            'strength2': 'Agility',
            'strength3': 'Wall Crawling',
            'weakness1': 'Impulsiveness',
            'weakness2': 'No Money',
            'weakness3': 'Guilt'
        }


class BlackPantherView(TemplateView):
    template_name = "phototest.html"

    def get_context_data(self, **kwargs):
        return {
            'title': "Black Panther",
            'image': '/static/images/blackPanther.png',
            'strength1': 'Superhuman Strength',
            'strength2': 'Knowledge and Wisdom ',
            'strength3': 'Vibranium',
            'weakness1': 'Responsibility as King',
            'weakness2': 'Magic',
            'weakness3': 'Emotions',

        }


class BlackWidowView(TemplateView):
    template_name = "phototest.html"

    def get_context_data(self, **kwargs):
        return {
            'title': 'Black Widow',
            'image': '/static/images/black_widow.jpg',
            'strength1': 'Martial Arts',
            'strength2': 'Highly trained Spy',
            'strength3': 'Speed and Athleticism',
            'weakness1': 'Brainwashing',
            'weakness2': 'Human',
            'weakness3': 'Cliff',
        }


class IronManView(TemplateView):
    template_name = "phototest.html"

    def get_context_data(self, **kwargs):
        return {
            'title': 'Iron Man',
            'image': '/static/images/iron_man.jpg',
            'strength1': 'Super-Genius Intellect',
            'strength2': 'Iron-Man suit',
            'strength3': 'Money',
            'weakness1': 'Alcohol',
            'weakness2': 'Girls',
            'weakness3': 'Dependence on Technology',
        }


class WinterSoldierView(TemplateView):
    template_name = "phototest.html"

    def get_context_data(self, **kwargs):
        return {
            'title': 'Winter Soldier',
            'image': '/static/images/wintersoldier.jpg',
            'strength1': 'Super Strength',
            'strength2': 'Expert Marksman',
            'strength3': 'Highly Trained Assassin',
            'weakness1': 'Brainwashing',
            'weakness2': 'Trauma',
            'weakness3': 'Mind Control',
        }
