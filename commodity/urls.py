from django.urls import path
from.views import BagView, SearchView

urlpatterns = [
    path('bag/', BagView, name='bag'),
    path('search/', SearchView, name='search'),
]