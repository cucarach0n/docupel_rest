from django.db import models

class Rol(models.Model):
    idRol = models.AutoField(primary_key = True)
    nombreRol = models.CharField('Nombre rol',max_length=100,null = False, blank = False)
    descripcionRol = models.CharField('Descripcion',max_length=255,null = True, blank = True)
    colorRol = models.CharField('Color rol',max_length=7,null = True, blank = True)
    fechaCreacion = models.DateTimeField("Fecha de creacion",auto_now_add=True)
    fechaUpdate = models.DateTimeField("Fecha de actualizacion",auto_now=True)
    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'

    #REQUIRED_FIELDS = ['correo']

    def __str__(self):
        return f'Rol {self.nombreRol} con el id {self.idRol}'


class Permiso(models.Model):
    idPermiso = models.AutoField(primary_key = True)
    nombrePermiso = models.CharField('Nombres',max_length=100,null = False, blank = False)
    descripcionPermiso = models.ImageField('Imagen de perfil', upload_to='avatars/', default="avatars/avataruni.png",max_length=255, null=True, blank = True)
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
    idRol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    idPermiso = models.ForeignKey(Permiso, on_delete=models.CASCADE)
    fechaCreacion = models.DateTimeField("Fecha de creacion",auto_now_add=True)
    fechaUpdate = models.DateTimeField("Fecha de actualizacion",auto_now=True)
    estado = models.BooleanField("Default", default=False)

    class Meta():
        verbose_name = 'PermisoRol'
        verbose_name_plural = 'PermisoRoles'
    
    def __str__(self):
        return "PermisoId {1} con RolId {0}".format(self.idPermiso,self.idRol)        