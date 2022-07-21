from django.db import models
#from apps.usuario.models import User
#from apps.accesoTeam.models import RolTeam
class Team(models.Model):
    idTeam = models.AutoField(primary_key = True)
    nombreTeam = models.CharField('Nombre rol',max_length=150,null = False, blank = False)
    iconoTeam = models.ImageField('Imagen del team', upload_to='teamIcono', default="teamIcono/defaultIcono.png",max_length=255, null=True, blank = True)
    imagenFondo = models.ImageField('Fondo del team', upload_to='teamBackground/', default="teamBackground/defaultBackground.png",max_length=255, null=True, blank = True)
    descripcionTeam = models.CharField('Descripcion',max_length=255,null = True, blank = True)
    tipoTeam = models.CharField('Tipo de team',max_length=1,null = False, blank = False,default="1")
    estadoTeam = models.BooleanField("Estado", default=True)
    fechaCreacion = models.DateTimeField("Fecha de creacion",auto_now_add=True)
    fechaUpdate = models.DateTimeField("Fecha de actualizacion",auto_now=True)
    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self):
        return f'Team {self.nombreTeam} con el id {self.idTeam}'

class TeamUsuario(models.Model):
    idTeamUsuario = models.AutoField(primary_key = True)
    username = models.CharField('Nombre rol',max_length=150,null = False, blank = False)
    imagenPerfil = models.ImageField('Imagen del Perfil', upload_to='perfil', default="perfil/defaultPerfil.png",max_length=255, null=True, blank = True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    usuario = models.ForeignKey("usuario.user", on_delete=models.CASCADE)
    fechaCreacion = models.DateTimeField("Fecha de creacion",auto_now_add=True)
    fechaUpdate = models.DateTimeField("Fecha de actualizacion",auto_now=True)
    class Meta:
        verbose_name = 'Team Usuario'
        verbose_name_plural = 'Team Usuarios'

    def __str__(self):
        return f'Perfil {self.username} con el id {self.idTeamUsuario}'

class RolUsuario(models.Model):
    idRolUsuario = models.AutoField(primary_key = True)
    teamUsuario = models.ForeignKey(TeamUsuario, on_delete=models.CASCADE)
    rolTeam = models.ForeignKey("accesoTeam.rolteam", on_delete=models.CASCADE)
    fechaCreacion = models.DateTimeField("Fecha de creacion",auto_now_add=True)
    fechaUpdate = models.DateTimeField("Fecha de actualizacion",auto_now=True)
    class Meta:
        verbose_name = 'Rol Usuario'
        verbose_name_plural = 'Roles Usuarios'

    def __str__(self):
        return f'Rol {self.idRolUsuario}'


