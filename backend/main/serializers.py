from .models import Player
from rest_framework import serializers


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'
