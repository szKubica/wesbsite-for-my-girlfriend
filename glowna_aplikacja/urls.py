from django.urls import path
from glowna_aplikacja.views import home, o_szkole, cennik, kontakt, nauczyciele

urlpatterns = [
    path('', home, name='home'),
    path('o_szkole/', o_szkole, name='o_szkole'),
    path('cennik/', cennik, name='cennik'),
    path('kontakt/', kontakt, name='kontakt'),
    path('nauczyciele/', nauczyciele, name='nauczyciele')
    ]