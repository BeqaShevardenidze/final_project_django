from django.urls import path, include
from users.views import Register
from .views import itjobs

urlpatterns = [
    path('', itjobs, name='itjobs'),
]