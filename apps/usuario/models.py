from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):
    def _create_user(self, correo,username,dni,genero,numeroTelefono,tipoCuenta,habilitado, password, is_superuser,**extra_fields):
        user = self.model(
            correo = correo,
            username = username,
            dni = dni,
            genero = genero,
            numeroTelefono = numeroTelefono,
            tipoCuenta = tipoCuenta,
            habilitado = habilitado,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self,username,dni,genero,numeroTelefono,tipoCuenta, correo,habilitado, password=None, **extra_fields):
        return self._create_user( correo,username,dni,genero,numeroTelefono,tipoCuenta,habilitado, password,False, **extra_fields)

    def create_superuser(self, correo,username,dni,genero,numeroTelefono,tipoCuenta,habilitado, password=None,**extra_fields):
        return self._create_user(correo,username,dni,genero,numeroTelefono,tipoCuenta, habilitado, password,True,**extra_fields)

class User(AbstractBaseUser, PermissionsMixin):

    #nombreUsuario = models.CharField('Usuario',max_length = 255, unique = True)
    correo = models.EmailField('Correo Electrónico',max_length = 255, unique = True)
    avatar = models.ImageField('Imagen de perfil', upload_to='avatars/', default="avatars/avataruni.png",max_length=255, null=True, blank = True)
    username = models.CharField('Username',max_length=260,null = False, blank = False)
    dni = models.CharField('Dni',max_length=8, null=False, blank = False, unique = True)
    genero = models.CharField('Genero',max_length=1,null = False, blank = False)
    numeroTelefono = models.CharField('Numero Telefono',max_length=12,null = True, blank = True)
    tipoCuenta = models.CharField('Tipo de cuenta',max_length=1,null = True, blank = True,default='0')
    fechaCreacion = models.DateTimeField("Fecha de creacion",auto_now_add=True)
    fechaUpdate = models.DateTimeField("Fecha de actualizacion",auto_now=True)
    habilitado = models.BooleanField(default = True)
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'correo'
    #REQUIRED_FIELDS = ['correo']

    def __str__(self):
        return f'Usuario {self.username} con el correo {self.correo}'


'''class teamUsuario(models.Model):
    idTeamUsuario = models.AutoField(primary_key = True)
    username = models.CharField('Nombres',max_length=100,null = False, blank = False)
    fechaCreacion = models.DateTimeField("Fecha de creacion",auto_now_add=True)
    fechaUpdate = models.DateTimeField("Fecha de actualizacion",auto_now=True)
    usuario = models.ForeignKey("User", on_delete=models.CASCADE)

    class Meta():
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
    
    def __str__(self):
        return "usuario {1} con el id {0}".format(self.idPerfil,self.nombres)'''