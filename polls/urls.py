from django.urls import path

from . import views

# Define the url for homepage
urlpatterns = [
    path("", views.index, name="index"),
]