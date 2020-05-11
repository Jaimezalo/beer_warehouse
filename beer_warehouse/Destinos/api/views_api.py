from rest_framework import viewsets

from serializers import BeerSerializer, CompanySerializer
from beer_warehouse.beers.models import Destino, Company


class BeerViewSet(viewsets.ModelViewSet):
    queryset = Destino.objects.all()
    serializer_class = BeerSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
