from django.urls import path, include
from . import views

# from django.views.generic import TemplateView

urlpatterns = [
    path('', views.fiqtest, name='iqtest'),
    path('oldscore/', views.oldscore, name='oldscore'),
]