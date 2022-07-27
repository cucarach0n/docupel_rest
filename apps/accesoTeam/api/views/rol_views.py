from apps.accesoTeam.api.serializers.permisoRol_serializers import PermisoRolListaSerializer
from rest_framework.response import Response
from apps.accesoTeam.models import Permiso, PermisoRol
from apps.accesoTeam.api.serializers.rol_serializers import RolTeamCreateSerializer, RolTeamListerializer, RolTeamQuerySerializer
from rest_framework import viewsets
from rest_framework import status
from datetime import datetime
from django.utils.crypto import get_random_string
from django.conf import settings
from apps.usuario.authentication_mixings import Authentication
from apps.utilidades.validadorPermiso import validarPermisos

def asignarPermisosDefault(rolTeam):
    permisosList = Permiso.objects.filter(default = True)
    for permiso in permisosList:
        permisoRol_obj = PermisoRol.objects.create(rol=rolTeam,permiso=permiso,activo=True)
        permisoRol_obj.save()

class RolTeamViewSet(Authentication,viewsets.GenericViewSet):
    serializer_class = RolTeamCreateSerializer
    def get_queryset(self,team):
        return self.serializer_class.Meta.model.objects.filter(team = team,tipoRol = '0')
    
    def list(self,request):
        Permisos = ['roles']
        rolTeam_serializer = RolTeamQuerySerializer(data = request.data)
        if rolTeam_serializer.is_valid():
            if(validarPermisos(Permisos,self.userFull,rolTeam_serializer.validated_data['team'])):
                queryset = self.get_queryset(rolTeam_serializer.validated_data['team'])
                serializer = RolTeamListerializer(queryset,many=True)
                return Response(serializer.data, status = status.HTTP_200_OK)
            else:
                return Response({"mensaje":"No tiene permisos para listar los roles"}, status = status.HTTP_403_FORBIDDEN)
        return Response(rolTeam_serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    def create(self,request):
        Permisos = ['roles']
        rolTeam_serializer = self.serializer_class(data = request.data)
        if rolTeam_serializer.is_valid():
            if(validarPermisos(Permisos,self.userFull,rolTeam_serializer.validated_data['team'])):
                rolTeam_obj = rolTeam_serializer.save()
                asignarPermisosDefault(rolTeam_obj)
                return Response(rolTeam_serializer.data, status = status.HTTP_201_CREATED )
            else:
                return Response({"mensaje":"No tiene permisos para crear un rol"}, status = status.HTTP_403_FORBIDDEN)
        return Response(rolTeam_serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
