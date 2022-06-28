from django.urls import path
from . import views
from .views import ContactView

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
]