from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):
    def _create_user(self, correo, fechaUpdate,habilitado, password, **extra_fields):
        user = self.model(
            correo = correo,
            fechaUpdate = fechaUpdate,
            habilitado = habilitado,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, correo, fechaUpdate,habilitado, password=None, **extra_fields):
        return self._create_user( correo, fechaUpdate,habilitado, password, **extra_fields)

    def create_superuser(self, correo, fechaUpdate,habilitado, password=None, **extra_fields):
        return self._create_user(correo, fechaUpdate, habilitado, password,**extra_fields)

class User(AbstractBaseUser, PermissionsMixin):

    #nombreUsuario = models.CharField('Usuario',max_length = 255, unique = True)
    correo = models.EmailField('Correo Electrónico',max_length = 255, unique = True,)
    fechaUpdate = models.DateTimeField("Fecha de actualizacion",auto_now=True)
    habilitado = models.BooleanField(default = False)
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'correo'
    #REQUIRED_FIELDS = ['correo']

    def __str__(self):
        return f'{self.correo}'


class Perfil(models.Model):
    idPerfil = models.AutoField(primary_key = True)
    nombres = models.CharField('Nombres',max_length=100,null = False, blank = False)
    imagenPerfil = models.ImageField('Imagen de perfil', upload_to='avatars/', default="avatars/avataruni.png",max_length=255, null=True, blank = True)
    apellidos = models.CharField('Apellidos',max_length=150,null = False, blank = False)
    genero = models.CharField('Genero',max_length=1,null = False, blank = False)
    fechaCreacion = models.DateTimeField("Fecha de creacion",auto_now_add=True)
    fechaUpdate = models.DateTimeField("Fecha de actualizacion",auto_now=True)
    usuario = models.ForeignKey("User", on_delete=models.CASCADE)

    class Meta():
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
    
    def __str__(self):
        return "usuario {1} con el id {0}".format(self.idPerfil,self.nombres)