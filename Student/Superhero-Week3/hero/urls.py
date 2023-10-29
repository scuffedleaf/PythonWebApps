from django.urls import path
from .views import WinterSoldierView, SpiderManView, IndexView, BlackPantherView
from django.contrib.admin import site

urlpatterns = [
    path('', IndexView.as_view()),
    path('spiderman', SpiderManView.as_view()),
    path('blackpanther', BlackPantherView.as_view()),
    path('wintersoldier', WinterSoldierView.as_view()),
    path(r'admin/', site.urls),

     #xsza matias is the coolest mfer on the planet
]
