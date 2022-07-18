from rest_framework import serializers
from apps.usuario.models import User

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['correo','name','last_name','avatar','is_staff','is_superuser','is_active']
    def validate_avatar(self,value):
        return value
    def validate(self,data):
        print('usuario token validado!')
        return data
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = ['name']
        exclude = ('password','last_login',)
    def to_representation(self,instance):
        return {
        "id": instance.id,
        "correo": instance.correo,
        "is_superuser": instance.is_superuser,
        "last_login": instance.last_login,
        "fechaUpdate": instance.fechaUpdate,
        "habilitado": instance.habilitado
    }
class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('id','habilitado','last_login','is_superuser',)                
    #def validate_correo(self, value):
    #    if '@fip.uni.edu.pe' not in value and '@uni.edu.pe' not in value:
    #        raise serializers.ValidationError('Error, el correo no es valido para esta institucion')
    #    return value
    def validate(self,data):
        #if data['nombreUsuario'] in data['contrasena']:
        #    raise serializers.ValidationError('El nombre de usuario no puede ser igual a la contrasena')
        return data
    def create(self,validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self,instance,validated_data):
        user_actualisado = super().update(instance,validated_data)

        user_actualisado.set_password(validated_data['password'])
        user_actualisado.save()
        return user_actualisado
class UserUpdateSerializer(serializers.Serializer):
    #history_id = serializers.CharField()
    name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField(allow_blank=True)
    avatar = serializers.ImageField(allow_null=True)
    class Meta:
        model = User
    
    def validate(self,data):
        #if data['nombreUsuario'] in data['contrasena']:
        #    raise serializers.ValidationError('El nombre de usuario no puede ser igual a la contrasena')
        return data
    def update(self,instance,validated_data):
        user_actualisado = super().update(instance,validated_data)
        if validated_data['password'] != None:
            user_actualisado.set_password(validated_data['password'])
        user_actualisado.save()
        return user_actualisado
class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id']
    def validate(self,data):
        return data
class UserDisabledSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','is_active']
    def validate(self,data):
        return data

