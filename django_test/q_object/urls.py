from django.urls import path
from q_object import views

urlpatterns = [
    path('qobj/', views.q_obj),
]
