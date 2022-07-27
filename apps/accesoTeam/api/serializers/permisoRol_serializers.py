from dataclasses import fields
from apps.workspace.models import Team
from rest_framework import serializers
from apps.accesoTeam.models import Permiso, PermisoRol, RolTeam

class PermisoRolListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermisoRol
        fields = '__all__'

class PermisoRolTeamSerializer(serializers.Serializer):
    rol = serializers.IntegerField(required=False)
    team = serializers.IntegerField(required=True)
    def validate_rol(self, rol=None):
        rol_obj = RolTeam.objects.get(idRolTeam=rol)
        if rol_obj:
            return rol_obj
        else:
            raise serializers.ValidationError("El rol no existe")
    def validate_team(self, team=None):
        team_obj = Team.objects.get(idTeam=team)
        if team_obj:
            return team_obj
        else:
            raise serializers.ValidationError("El team no existe")
class PermisoRolCreateSerializer(serializers.Serializer):
           
    #id = serializers.IntegerField()
    #history_id = serializers.CharField()
    rol = serializers.IntegerField()
    permiso = serializers.IntegerField()
    activo = serializers.BooleanField()
    team = serializers.IntegerField()

    def validate_rol(self, rol):
        rol_obj = RolTeam.objects.get(idRolTeam=rol)
        if rol_obj:
            return rol_obj
        else:
            raise serializers.ValidationError("El rol no existe")
    def validate_permiso(self, permiso):
        permiso_obj = Permiso.objects.get(idPermiso=permiso)
        if permiso_obj:
            return permiso_obj
        else:
            raise serializers.ValidationError("El permiso no existe")
    def validate_team(self, team):
        team_obj = Team.objects.get(idTeam=team)
        if team_obj:
            return team_obj
        else:
            raise serializers.ValidationError("El team no existe")
    def validate(self, data):
        permisoRol_obj = PermisoRol.objects.filter(rol=data['rol'],permiso=data['permiso'])
        if permisoRol_obj:
            raise serializers.ValidationError("Ya se encuentra registrado este permiso para este rol")
        return data
    def create(self,validated_data):
        permisoRol_obj = PermisoRol.objects.create(rol=validated_data["rol"],permiso=validated_data["permiso"],activo=validated_data["activo"])
        #permisoRol_obj.save()
        return permisoRol_obj