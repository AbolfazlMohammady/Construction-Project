from django.urls import path

from .views import HomePageView, ContactView, AboutPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", ContactView.as_view(), name="contact"),
]
