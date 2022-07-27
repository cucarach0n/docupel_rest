from django.db import models
#from apps.workspace.models import Team
class RolTeam(models.Model):
    idRolTeam = models.AutoField(primary_key = True)
    nombreRol = models.CharField('Nombre rol',max_length=100,null = False, blank = False)
    descripcionRol = models.CharField('Descripcion',max_length=255,null = True, blank = True)
    colorRol = models.CharField('Color rol',max_length=7,null = True, blank = True)
    fechaCreacion = models.DateTimeField("Fecha de creacion",auto_now_add=True)
    fechaUpdate = models.DateTimeField("Fecha de actualizacion",auto_now=True)
    team = models.ForeignKey("workspace.team", on_delete=models.CASCADE)
    tipoRol = models.CharField('Tipo rol',max_length=1,null = False, blank = False,default='0')
    class Meta:
        verbose_name = 'Rol Team'
        verbose_name_plural = 'Roles Teams'

    #REQUIRED_FIELDS = ['correo']

    def __str__(self):
        return f'Rol {self.nombreRol} con el id {self.idRolTeam}'


class Permiso(models.Model):
    idPermiso = models.AutoField(primary_key = True)
    nombrePermiso = models.CharField('Nombres',max_length=100,null = False, blank = False)
    descripcionPermiso = models.CharField('Descripcion permiso',max_length=255,null = True, blank = True)
    fechaCreacion = models.DateTimeField("Fecha de creacion",auto_now_add=True)
    fechaUpdate = models.DateTimeField("Fecha de actualizacion",auto_now=True)
    default = models.BooleanField("Default", default=False)

    class Meta():
        verbose_name = 'Permiso'
        verbose_name_plural = 'Permisos'
    
    def __str__(self):
        return "Permiso {1} con el id {0}".format(self.nombrePermiso,self.idPermiso)

class PermisoRol(models.Model):
    idPermisoRol = models.AutoField(primary_key = True)
    rol = models.ForeignKey(RolTeam, on_delete=models.CASCADE)
    permiso = models.ForeignKey(Permiso, on_delete=models.CASCADE)
    fechaCreacion = models.DateTimeField("Fecha de creacion",auto_now_add=True)
    fechaUpdate = models.DateTimeField("Fecha de actualizacion",auto_now=True)
    activo = models.BooleanField("Default", default=False)
    class Meta():
        verbose_name = 'PermisoRol'
        verbose_name_plural = 'PermisoRoles'
    
    def __str__(self):
        return "PermisoId {0} con RolId {1}".format(self.idPermisoRol,self.rol)        