from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="base-home"),
    path("about/", views.about, name="base-about"),
    path("team/", views.team, name="base-team"),
    path("partners/", views.partners, name="base-partners"),
    path("contact/", views.contact, name="base-contact"),
]
