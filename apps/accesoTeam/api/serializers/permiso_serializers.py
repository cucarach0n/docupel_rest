from rest_framework import serializers
from apps.accesoTeam.models import Permiso

class PermisoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permiso
        fields = '__all__'
    def to_representation(self,instance):
        return {
        "idPermiso": instance.idPermiso,
        "nombrePermiso": instance.nombrePermiso,
        "descripcionPermiso": instance.descripcionPermiso,
        "activo": instance.default,
    }