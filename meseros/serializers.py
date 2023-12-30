# meseros/serializers.py

from rest_framework import serializers
from .models import Meseros

class MeseroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meseros
        fields = ['nombre', 'edad', 'nacionalidad', 'dni' ]
