from apps.workspace.models import Team, TeamUsuario

def getCantidadTeamPorUsuario(usuario):
    cantidad = TeamUsuario.objects.filter(usuario=usuario).count()
    return cantidad
def getStorageTeamPorUsuario(usuario):
    storageActual = 0
    teams = Team.objects.filter(teamusuario__usuario=usuario)
    for team in teams:
        storageActual += team.maxStorage
    return storageActual