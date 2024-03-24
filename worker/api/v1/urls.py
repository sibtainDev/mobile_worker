from django.urls import path
from .views import get_units_by_worker, make_visit

urlpatterns = [
    path('get_units/', get_units_by_worker, name='get_units'),
    path('make_visit/', make_visit, name='make_visit'),
]