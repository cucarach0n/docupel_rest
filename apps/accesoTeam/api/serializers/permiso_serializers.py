from rest_framework import serializers
from apps.accesoTeam.models import Permiso

class PermisoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permiso
        fields = '__all__'