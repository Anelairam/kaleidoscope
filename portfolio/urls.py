from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('product_management/', views.productmng, name='product_management'),
]