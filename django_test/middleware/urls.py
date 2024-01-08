from django.urls import path
from middleware import views
urlpatterns = [
    path('fbv_middleware/',views.myview),
    ]