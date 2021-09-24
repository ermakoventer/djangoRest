from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import FilmsViewSet
from  . import  views


router = SimpleRouter()
router.register('api/films', FilmsViewSet)

urlpatterns = [
    path('', views.all_films)
]

urlpatterns += router.urls