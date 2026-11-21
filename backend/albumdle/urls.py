from django.urls import path
from . import views
urlpatterns = [
    path('api/albums/add', views.add_album),
    path('api/albums/load', views.load_album)
]