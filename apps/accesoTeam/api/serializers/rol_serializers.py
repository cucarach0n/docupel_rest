from dataclasses import field
from apps.accesoTeam.api.serializers.permisoRol_serializers import PermisoRolListaSerializer
from apps.accesoTeam.api.serializers.permiso_serializers import PermisoListSerializer
from rest_framework import serializers
from apps.accesoTeam.models import Permiso, RolTeam
from django.db.models import Q

class RolTeamCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolTeam
        exclude = ('idRolTeam','fechaCreacion','fechaUpdate',)
class RolTeamQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = RolTeam
        fields = ['team']
class RolTeamUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolTeam
        exclude = ('idRolTeam','fechaCreacion','fechaUpdate','team','tipoRol',)
class RolTeamListerializer(serializers.ModelSerializer):
    class Meta:
        model = RolTeam
        fields = '__all__'
    def to_representation(self,instance):
        permisos = Permiso.objects.filter(permisorol__rol=instance.idRolTeam)
        permisosAll = Permiso.objects.filter(~Q(permisorol__rol = instance.idRolTeam))
        arrayPermiso = []
        for permi in permisos:
            permi.default = True
            arrayPermiso.append(permi)
        for permiso in permisosAll:
            permiso.default = False
            arrayPermiso.append(permiso)
        permisos |= permisosAll

        return {
        "idRolTeam": instance.idRolTeam,
        "nombreRol": instance.nombreRol,
        "descripcionRol": instance.descripcionRol,
        "colorRol": instance.colorRol,
        "fechaCreacion": instance.fechaCreacion,
        "fechaUpdate": instance.fechaUpdate,
        "permisos": PermisoListSerializer(arrayPermiso,many = True).data
    }