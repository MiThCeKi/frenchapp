from django.urls import path
from . import views

urlpatterns = [
    path('index/<str:attempt>', views.index, name='index')
]