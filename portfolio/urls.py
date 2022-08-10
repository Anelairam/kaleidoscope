from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('<photo_id>', views.photo_detail, name='photo_detail'),
]