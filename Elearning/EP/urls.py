from django.urls import path, include
from .views import IndexView, Forms,   show
urlpatterns = [
    path("", IndexView, name='index'),
    path('Forms/', Forms,  name='forms' ),
    path('show/', show, name='show' ),
]