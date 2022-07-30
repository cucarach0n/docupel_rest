from apps.accesoTeam.api.serializers.permisoRol_serializers import PermisoRolListaSerializer
from rest_framework.response import Response
from apps.accesoTeam.models import Permiso, PermisoRol
from apps.accesoTeam.api.serializers.rol_serializers import RolTeamCreateSerializer, RolTeamListerializer, RolTeamQuerySerializer, RolTeamUpdateSerializer
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
    def get_queryset(self,team = None):
        if team is not None:
            return self.serializer_class.Meta.model.objects.filter(team = team,tipoRol__in = ['0','1'])
        return None
    def list(self,request):
        '''
        Obtener roles en el team

        parametros
        - teamId int

        test
        '''
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
        '''
        Crear un rol

        parametros
        - nombreRol varchar(100)
        - descripcionRol varchar(255)
        - colorRol varchar(7)
        - teamId    int
        '''
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
    def update(self,request,pk = None):
        '''
        Actualizar un rol

        parametro por url /rolId/
        - rolId int

        parametros
        - nombreRol varchar(100)
        - descripcionRol varchar(255)
        - colorRol varchar(7)
        '''
        Permisos = ['roles']
        rolTeam_obj = self.serializer_class.Meta.model.objects.get(idRolTeam = pk,tipoRol__in = ['0','1'])
        if rolTeam_obj:
            rolTeam_serializer = RolTeamUpdateSerializer(data = request.data,instance = rolTeam_obj)
            if rolTeam_serializer.is_valid():
                if(validarPermisos(Permisos,self.userFull,rolTeam_obj.team)):
                    rolTeam_obj = rolTeam_serializer.save()
                    return Response(rolTeam_serializer.data, status = status.HTTP_200_OK)
                else:
                    return Response({"mensaje":"No tiene permisos para actualizar un rol"}, status = status.HTTP_403_FORBIDDEN)
            return Response(rolTeam_serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        return Response({"mensaje":"No existe el rol"}, status = status.HTTP_404_NOT_FOUND)
    def destroy(self,request,pk = None):
        '''
        Eliminar un rol

        parametros en url /id/
        - idRolTeam int
        '''
        Permisos = ['roles']
        rolTeam_obj = self.serializer_class.Meta.model.objects.get(idRolTeam = pk,tipoRol__in = ['0','1'])
        if rolTeam_obj:
            if(validarPermisos(Permisos,self.userFull,rolTeam_obj.team)):
                rolTeam_obj.delete()
                return Response({"mensaje":"Rol eliminado"}, status = status.HTTP_200_OK)
            else:
                return Response({"mensaje":"No tiene permisos para eliminar un rol"}, status = status.HTTP_403_FORBIDDEN)
        return Response({"mensaje":"No existe el rol"}, status = status.HTTP_404_NOT_FOUND)
    
