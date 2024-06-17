from django.urls import path, include
from .views import theme

urlpatterns = [
    path('', theme),
]