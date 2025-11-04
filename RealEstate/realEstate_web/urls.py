from django.urls import path
from . import views
app_name = "main"

urlpatterns = [
    path("", views.home, name="home"),
    path("properties/", views.properties, name="properties"),
    path("contact/", views.contact, name="contact"),
    path('toggle_dark_mode/', views.toggle_dark_mode, name='toggle_dark_mode'),
]