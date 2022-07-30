from django.db import models
#from apps.usuario.models import User
#from apps.accesoTeam.models import RolTeam
class Team(models.Model):
    idTeam = models.AutoField(primary_key = True)
    nombreTeam = models.CharField('Nombre rol',max_length=150,null = False, blank = False)
    iconoTeam = models.ImageField('Imagen del team', upload_to='teamIcono/', default="teamIcono/defaultIcono.png",max_length=255, null=True, blank = True)
    imagenFondo = models.ImageField('Fondo del team', upload_to='teamBackground/', default="teamBackground/defaultBackground.png",max_length=255, null=True, blank = True)
    descripcionTeam = models.CharField('Descripcion',max_length=255,null = True, blank = True)
    tipoTeam = models.CharField('Tipo de team',max_length=1,null = True, blank = True,default="0")
    estadoTeam = models.BooleanField("Estado", default=True)
    maxStorage = models.IntegerField("Maximo de storage", default=5)#capacidad en Gb
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
    imagenPerfil = models.ImageField('Imagen del Perfil', upload_to='perfil/', default="perfil/defaultPerfil.png",max_length=255, null=True, blank = True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    usuario = models.ForeignKey("usuario.user", on_delete=models.CASCADE)
    owner = models.BooleanField("Es el owner", default=False)
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


class InvitacionTeam(models.Model):
    idInvitacionTeam = models.AutoField(primary_key = True)
    fechaCreacion = models.DateTimeField("Fecha de creacion",auto_now_add=True)
    tipoInvitacion = models.CharField('Tipo de invitacion',max_length=1,null = True, blank = True,default="0")
    cantidadInvitacion = models.IntegerField("Saldo de invitacion", default=0)
    fechaExpiracion = models.DateTimeField("Fecha de expiracion",null = True, blank = True)
    slugInvitacion = models.SlugField(unique=True, max_length=11, blank=True, null=True)
    teamUsuario = models.ForeignKey(TeamUsuario, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Invitacion Team'
        verbose_name_plural = 'Invitaciones Teams'

    def __str__(self):
        return f'Invitacion {self.idInvitacionTeam} creado para el team {self.teamUsuario.team.nombreTeam}'

class InvitacionUsuario(models.Model):
    idInvitacionUsuario = models.AutoField(primary_key = True)
    invitacionTeam = models.ForeignKey(InvitacionTeam, on_delete=models.CASCADE)
    usuario = models.ForeignKey("usuario.user", on_delete=models.CASCADE)
    fechaUnion = models.DateTimeField("Fecha de union",null = True, blank = True)
    class Meta:
        verbose_name = 'Invitacion Usuario'
        verbose_name_plural = 'Invitaciones Usuarios'

    def __str__(self):
        return f'InvitacionUsuarioId {self.idInvitacionUsuario} se unio el usuario {self.usuario.username}'