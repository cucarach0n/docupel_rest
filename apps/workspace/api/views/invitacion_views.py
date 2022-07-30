
from apps.usuario.authentication_mixings import Authentication
from apps.workspace.api.serializers.invitacion_serializers import InvitacionCreateSerializer
from rest_framework import viewsets

class TeamViewSet(Authentication,viewsets.GenericViewSet):
    serializer_class = InvitacionCreateSerializer
    def get_queryset(self,slug = None):
        if slug is not None:
            return self.serializer_class.Meta.model.objects.filter(slugInvitacion = slug)
        return None
    def create(self,request):
        '''
        Crear invitacion

        parametros
        - 
        '''