"""URL endpoints for the get_endpoints app"""

from django.urls import path
from . import views

urlpatterns = [
    path("api/info", views.InformationView.as_view(), name="get_info_endpoint"),
    path('api/', views.PersonListCreateView.as_view(), name='person-list-create'),
    path('api/<int:pk>/', views.PersonDetailView.as_view(), name='person-detail'),
]


