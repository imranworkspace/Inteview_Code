from django.urls import path
from mystatic import views

urlpatterns = [
    path('static/',views.mystat),
    ]