from django.urls import path
from . import views

urlpatterns = [
    path('index/<int:guessed_number>', views.index, name='index')
]