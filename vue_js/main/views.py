from django.shortcuts import render
from .models import Film
from rest_framework.viewsets import ModelViewSet
from .serializers import FilmSerializer


class FilmsViewSet(ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


def all_films(request):
    return render(request, 'main/main.html')
