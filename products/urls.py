from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
    path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'
    ),
]