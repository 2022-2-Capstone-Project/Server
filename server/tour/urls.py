from django.urls import path
from .views import getTourList

urlpatterns = [
    path("tourlist/", getTourList)
]