from dataclasses import field
from apps.accesoTeam.api.serializers.permisoRol_serializers import PermisoRolListaSerializer
from apps.accesoTeam.api.serializers.permiso_serializers import PermisoListSerializer
from rest_framework import serializers
from apps.accesoTeam.models import Permiso, RolTeam

class RolTeamCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolTeam
        exclude = ('idRolTeam','fechaCreacion','fechaUpdate',)
class RolTeamQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = RolTeam
        fields = ['team']
class RolTeamListerializer(serializers.ModelSerializer):
    class Meta:
        model = RolTeam
        fields = '__all__'
    def to_representation(self,instance):
        permisos = Permiso.objects.filter(permisorol__rol=instance.idRolTeam)
        return {
        "idRolTeam": instance.idRolTeam,
        "nombreRol": instance.nombreRol,
        "descripcionRol": str(instance.descripcionRol),
        "colorRol": instance.colorRol,
        "fechaCreacion": instance.fechaCreacion,
        "fechaUpdate": instance.fechaUpdate,
        "permisos": PermisoListSerializer(permisos,many = True).data
    }