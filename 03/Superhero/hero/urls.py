from django.urls import path
from .views import WinterSoldierView, SpiderManView, IndexView, BlackPantherView

urlpatterns = [
    path('', IndexView.as_view()),
    path('spiderman', SpiderManView.as_view()),
    path('blackpanther', BlackPantherView.as_view()),
    path('wintersoldier', WinterSoldierView.as_view()),

     #xsza matias is the coolest mfer on the planet
]
