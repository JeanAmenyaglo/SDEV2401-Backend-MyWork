from django.urls import path
from .views import home_page, pet_type_details, about_page

urlpatterns = [
    path("", home_page, name="home_page"),
    path("pet_type/<str:pet_type>/", pet_type_details, name="pet_type_details"),
    path("about/", about_page, name="about_page"),
]