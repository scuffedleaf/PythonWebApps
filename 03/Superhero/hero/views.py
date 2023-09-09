from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'heroes.html'


class SpiderManView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Spiderman',
            'body': "My name is Peter Parker, let's do this one last time",
            'image': '/static/images/spiderman1610.jpg'
        }


class BlackPantherView(TemplateView):
    template_name = "hero.html"

    def get_context_data(self, **kwargs):
        return {
            'title': 'Black Panther',
            'body': 'The living are not done with you. Wakanda Forever!',
            'image': '/static/images/blackPanther.png'
        }


class WinterSoldierView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Winter Soldier',
            'body': 'Ready to comply.',
            'image': '/static/images/wintersoldier.jpg'
        }
    