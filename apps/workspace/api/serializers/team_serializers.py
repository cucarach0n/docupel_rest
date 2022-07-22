from dataclasses import fields
from rest_framework import serializers
from apps.workspace.models import Team,TeamUsuario

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
        return {
        "idTeam": instance.idTeam,
        "nombreTeam": instance.nombreTeam,
        "iconoTeam": instance.iconoTeam.name,
        "imagenFondo": instance.imagenFondo.name,
        "descripcionTeam": instance.descripcionTeam,
        "estadoTeam": instance.estadoTeam,
        "maxStorage": instance.maxStorage,
        "cantidadUsuarios": cantidadUsuarios,
        "fechaCreacion": instance.fechaCreacion,
        "fechaUpdate": instance.fechaUpdate
    }
class TeamUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        exclude = ('idTeam','fechaCreacion','fechaUpdate','tipoTeam',)