from django.urls import path
from . import views

urlpatterns = [
    path('index/<str:datahere>', views.index, name='index')
]