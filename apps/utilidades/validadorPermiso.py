from apps.accesoTeam.models import RolTeam,Permiso

def validarPermisos(permisos,usuario,team):
    rolesUsuario = RolTeam.objects.filter(rolusuario__teamUsuario__usuario = usuario,team = team)
    for rol in rolesUsuario:
        permisoUsuario = Permiso.objects.filter(permisorol__rol = rol)
        for permiso in permisoUsuario:
            if(permiso.nombrePermiso.lower() in permisos):
                return True
    return False