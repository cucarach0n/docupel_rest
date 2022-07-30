from django.contrib import admin
from apps.workspace.models import *
# Register your models here.

admin.site.register(Team)
admin.site.register(TeamUsuario)
admin.site.register(RolUsuario)
admin.site.register(InvitacionTeam)
admin.site.register(InvitacionUsuario)
