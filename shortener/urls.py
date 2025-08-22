from django.urls import path
from shortener import views

urlpatterns = [
    path("", views.home, name="home"), 
]
