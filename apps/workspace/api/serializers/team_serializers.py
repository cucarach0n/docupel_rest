from dataclasses import fields
from apps.accesoTeam.api.serializers.rol_serializers import RolTeamListerializer
from apps.accesoTeam.models import RolTeam
from rest_framework import serializers
from apps.workspace.models import Team,TeamUsuario
from django.db.models import Q

class TeamCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        exclude = ('idTeam','fechaCreacion','fechaUpdate','estadoTeam','tipoTeam',)

    
class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        exclude = ('idTeam',)
class TeamDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
    def to_representation(self,instance):
        cantidadUsuarios = TeamUsuario.objects.filter(team = instance).count()
        rolTeams = RolTeam.objects.filter(tipoRol__in = ['0','1'],team = instance)
        
        return {
        "idTeam": instance.idTeam,
        "nombreTeam": instance.nombreTeam,
        "iconoTeam": instance.iconoTeam.name,
        "imagenFondo": instance.imagenFondo.name,
        "descripcionTeam": instance.descripcionTeam,
        "estadoTeam": instance.estadoTeam,
        "maxStorage": instance.maxStorage,
        "cantidadUsuarios": cantidadUsuarios,
        "roles": RolTeamListerializer(rolTeams,many = True).data,
        "fechaCreacion": instance.fechaCreacion,
        "fechaUpdate": instance.fechaUpdate
    }
class TeamUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        exclude = ('idTeam','fechaCreacion','fechaUpdate','tipoTeam',)