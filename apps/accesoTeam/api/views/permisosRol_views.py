from apps.accesoTeam.api.serializers.permisoRol_serializers import PermisoRolCreateSerializer, PermisoRolListaSerializer, PermisoRolTeamSerializer
from apps.accesoTeam.api.serializers.permiso_serializers import PermisoListSerializer
from rest_framework.response import Response
from apps.accesoTeam.models import Permiso, PermisoRol
from apps.accesoTeam.api.serializers.rol_serializers import RolTeamCreateSerializer
from rest_framework import viewsets
from rest_framework import status
from apps.usuario.authentication_mixings import Authentication
from apps.utilidades.validadorPermiso import validarPermisos


class PermisoRolViewSet(Authentication,viewsets.GenericViewSet):
    serializer_class = PermisoRolCreateSerializer
    def get_queryset(self,rolTeam = None):
        if rolTeam is not None:
            return PermisoRol.objects.filter(rol = rolTeam)
        return None
    def list(self,request):
        Permisos = ['roles']
        rolTeamPermiso_serializer = PermisoRolTeamSerializer(data = request.data)
        if rolTeamPermiso_serializer.is_valid():  
    
            if(validarPermisos(Permisos,self.userFull,rolTeamPermiso_serializer.validated_data['team'])):
                permisoRol_obj = Permiso.objects.filter(permisorol__rol=rolTeamPermiso_serializer.validated_data['rol'])
                if permisoRol_obj:
                    return Response(PermisoListSerializer(permisoRol_obj,many = True).data,status = status.HTTP_200_OK)
                return Response({'mensaje':'No existen permisos con el rol enviado'},status = status.HTTP_404_NOT_FOUND)
            else:
                return Response({"mensaje":"No tiene permisos para eliminar un rol"}, status = status.HTTP_403_FORBIDDEN)
        return Response(rolTeamPermiso_serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    def create(self,request):
        Permisos = ['roles']
        permisoRol_serializer = self.serializer_class(data = request.data)
        if permisoRol_serializer.is_valid():
            if(validarPermisos(Permisos,self.userFull,permisoRol_serializer.validated_data['team'])):
                permisoRol_obj = permisoRol_serializer.create(permisoRol_serializer.validated_data)
                permisoRol_obj.save()
                return Response(PermisoRolListaSerializer(permisoRol_obj).data, status = status.HTTP_201_CREATED )
            else:
                return Response({"mensaje":"No tiene permisos para crear un rol"}, status = status.HTTP_403_FORBIDDEN)
        return Response(permisoRol_serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    def destroy(self,request,pk=None):
        Permisos = ['roles']
        rolTeamPermiso_serializer = PermisoRolTeamSerializer(data = request.data)
        if rolTeamPermiso_serializer.is_valid():  
            if(validarPermisos(Permisos,self.userFull,rolTeamPermiso_serializer.validated_data['team'])):
                permisoRol_obj = PermisoRol.objects.filter(idPermisoRol = pk).first()
                if permisoRol_obj:
                    permisoRol_obj.delete()
                    return Response({'mensaje':'Eliminado correctamente'},status = status.HTTP_200_OK)
                return Response({'mensaje':'No existe el permiso'},status = status.HTTP_404_NOT_FOUND)
            else:
                return Response({"mensaje":"No tiene permisos para eliminar un rol"}, status = status.HTTP_403_FORBIDDEN)
        return Response(rolTeamPermiso_serializer.errors,status = status.HTTP_400_BAD_REQUEST)  