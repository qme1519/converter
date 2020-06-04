from django.urls import path
from . import views

# define url addresses to be used in the project
urlpatterns = [
    path("", views.index, name="index"),
    path("<type>/", views.conversion_types, name="conversion_types"),
]