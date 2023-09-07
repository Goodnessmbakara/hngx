"""URL endpoints for the get_endpoints app"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.InformationView.as_view(), name="get_info_endpoint"),
]
