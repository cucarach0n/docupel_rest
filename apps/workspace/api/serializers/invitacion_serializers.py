
from apps.workspace.models import InvitacionTeam
from rest_framework import serializers
from django.db.models import Q

class InvitacionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvitacionTeam
        exclude = ('idTeam','fechaCreacion','fechaUpdate','estadoTeam','tipoTeam',)