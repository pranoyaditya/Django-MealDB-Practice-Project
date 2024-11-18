from django.urls import path
from . import views

urlpatterns = [
    path('',views.display, name = 'meal_page'),
]