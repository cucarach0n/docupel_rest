from apps.workspace.models import Team
from rest_framework.response import Response
from apps.workspace.models import Team,TeamUsuario,RolUsuario
from apps.workspace.api.serializers.team_serializers import TeamCreateSerializer, TeamSerializer,TeamDetailSerializer
from rest_framework import viewsets
from rest_framework import status
from datetime import datetime
from django.utils.crypto import get_random_string
from django.conf import settings
from apps.usuario.authentication_mixings import Authentication
from apps.workspace.util import getStorageTeamPorUsuario,getCantidadTeamPorUsuario
from apps.accesoTeam.models import RolTeam,Permiso,PermisoRol

def crearRolesDefault(team,perfilAdmin):
    roles = [
        {'nombreRol':'ownerPerma','descripcionRol':'Dueño del team','colorRol':'#FF0000','team':team,'tipoRol':'2'},
        {'nombreRol':'everyone','descripcionRol':'Rol para todos los usuarios','colorRol':'#000000','team':team,'tipoRol':'1'}
    ]
    permisosList = Permiso.objects.all()
    for rol in roles:
        rol_obj = RolTeam.objects.create(**rol)
        rol_obj.save()
        if(rol_obj.nombreRol == 'ownerPerma'):
            for permiso in permisosList:
                permiso_obj = PermisoRol.objects.create(rol=rol_obj,permiso=permiso,activo=True)
                permiso_obj.save()
        else:
            for permiso in permisosList:
                if(permiso.default):
                    permiso_obj = PermisoRol.objects.create(rol=rol_obj,permiso=permiso,activo=True)
                    permiso_obj.save()
    
    rolUsuario = RolUsuario.objects.create(teamUsuario = perfilAdmin,rolTeam = RolTeam.objects.get(nombreRol='ownerPerma',team=team))
    rolUsuario.save()
    return True

class TeamViewSet(Authentication,viewsets.GenericViewSet):
    serializer_class = TeamCreateSerializer
    def get_queryset(self):
        return Team.objects.filter(teamusuario__usuario = self.userFull,teamusuario__owner = True)
    def list(self,request):
        teamList = self.get_queryset()
        team_serializer = TeamDetailSerializer(teamList,many = True)
        return Response(team_serializer.data, status = status.HTTP_200_OK )
    def create(self,request):
        team_serializer = self.serializer_class(data = request.data)
        if team_serializer.is_valid():
            flagCreate = False
            if(self.userFull.tipoCuenta != '0'):
                storageActual = getStorageTeamPorUsuario(self.userFull) + team_serializer.validated_data['maxStorage']
                
                if(self.userFull.tipoCuenta == '1' ):
                    
                    if(getCantidadTeamPorUsuario(self.userFull) < 1):
                        if(storageActual <= 5):
                            flagCreate = True
                        else:
                            return Response({"mensaje":"Supero los 5Gb de almacenamiento de su cuenta"},status = status.HTTP_403_FORBIDDEN)
                    else:
                        return Response({"mensaje":"Supero el limite de teams en su plan basico"},status = status.HTTP_403_FORBIDDEN)
                elif(self.userFull.tipoCuenta == '2'):
                    if(getCantidadTeamPorUsuario(self.userFull) < 3):
                        if(storageActual <= 15):
                           flagCreate = True
                        else:
                            return Response({"mensaje":"Supero los 15Gb de almacenamiento de su cuenta"},status = status.HTTP_403_FORBIDDEN)    
                    else:
                        return Response({"mensaje":"Supero el limite de teams en su plan normal"},status = status.HTTP_403_FORBIDDEN)
                elif(self.userFull.tipoCuenta == '3'):
                    if(storageActual <= 50):
                        flagCreate = True
                    else:
                        return Response({"mensaje":"Supero los 50Gb de almacenamiento de su cuenta"},status = status.HTTP_403_FORBIDDEN)
         
                           
                if(flagCreate):
                    team = team_serializer.save()
                    teamUsuarioObject = TeamUsuario.objects.create(usuario = self.userFull,
                                                team = team,
                                                username = self.userFull.username,
                                                imagenPerfil = self.userFull.avatar,
                                                owner = True)
                    
                    teamUsuarioObject.save()
                    crearRolesDefault(team,teamUsuarioObject)
                    return Response(TeamDetailSerializer(team).data,status = status.HTTP_201_CREATED)
                return Response({"mensaje":"Pan desconocido"},status = status.HTTP_418_IM_A_TEAPOT) 
            else:
                return Response({"mensaje":"No tienes permisos para crear un team"},status = status.HTTP_403_FORBIDDEN)
            
        return Response(team_serializer.errors,status = status.HTTP_400_BAD_REQUEST)
