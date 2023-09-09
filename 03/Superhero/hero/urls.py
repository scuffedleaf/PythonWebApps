from django.urls import path
from .views import WinterSoldierView, SpiderManView, IndexView, IronManView

urlpatterns = [
    path('', IndexView.as_view()),
    path('spiderman', SpiderManView.as_view()),
    path('ironman', IronManView.as_view()),
    path('wintersoldier', WinterSoldierView.as_view()),

     #xsza matias is the coolest mfer on the planet
]
