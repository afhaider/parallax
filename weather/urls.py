from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexzz,name='indexzz'),
]