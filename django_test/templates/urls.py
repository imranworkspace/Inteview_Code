from django.urls import path
from templates import views
urlpatterns = [
    path('home/',views.home),
    ]