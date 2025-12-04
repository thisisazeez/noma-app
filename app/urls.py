from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about_us/", views.about_us, name="about_us"),
    path("team/", views.team_view, name="team"),
    path("contact_us/", views.contact_view, name="contact_us"),
    path("gallery/", views.gallery_view, name="gallery"),
    path("our-work/", views.transformation_view, name="our_work"),
    path("coming-soon/", views.coming_soon, name="coming_soon"),
    path("innovative-agricultural-practices/", views.iap_view, name="iap"),
    path("places-impacted/", views.places_impacted, name="places_impacted"),
    path("robots.txt", views.robots_txt, name="robots_txt"),
]

