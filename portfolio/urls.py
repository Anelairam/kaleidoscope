from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('<photo_id>', views.photo_detail, name='photo_detail'),
    path('<onlinecourse_id>', views.onlinecourse_detail, name='onlinecourse_detail'),
    path('<tour_id>', views.tour_detail, name='tour_detail'),
]