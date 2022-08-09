from django.urls import path
from . import views

urlpatterns = [
    path('', views.eshop, name='eshop'),
]