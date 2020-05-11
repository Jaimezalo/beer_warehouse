from rest_framework import serializers

from beer_warehouse.beers.models import Destino, Company


class BeerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Destino
        fields = ('url', 'name', 'abv', 'color', 'is_filtered')


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'tax_number')
