from hero.views import PhotoDetailView, PhotoListView, SpidermanView, BlackPantherView, BlackWidowView, WinterSoldierView,IronManView
from django.views.generic import RedirectView
from django.contrib.admin import site
from django.contrib import admin
from django.urls import path
'''
urlpatterns = [
    path('admin/', admin.site.urls),
]


urlpatterns = [
    path(r'admin/', site.urls),
]
'''

urlpatterns = [

    # admin
    path(r'admin/', admin.site.urls),

    # Home
    path('', RedirectView.as_view(url='hero/')),

    # Photos
    path('hero/', PhotoListView.as_view()),
    path('hero/<int:id>', PhotoDetailView.as_view()),
    path('hero/spiderman', SpidermanView.as_view()),
    path('hero/blackpanther', BlackPantherView.as_view()),
    path('hero/blackwidow', BlackWidowView.as_view()),
    path('hero/ironman', IronManView.as_view()),
    path('hero/wintersoldier', WinterSoldierView.as_view()),
]
