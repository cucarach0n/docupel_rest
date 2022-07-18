from rest_framework import serializers
from apps.usuario.models import Perfil

class PerfilCreateSerializer(serializers.Serializer):
           
    #id = serializers.IntegerField()
    #history_id = serializers.CharField()"""
    nombres = serializers.CharField(allow_null=False)
    apellidos = serializers.CharField(allow_null=False)
    imagenPerfil = serializers.ImageField(allow_null=True)
    genero = serializers.CharField(allow_null=False)
    correo = serializers.CharField(allow_null=False)
    password = serializers.CharField(allow_null=False)
    """def create(self,validated_data):
        perfil = Perfil.objects.create(nombres=validated_data["nombres"],apellidos=validated_data["apellidos"],imagenPerfil=validated_data["imagenPerfil"],genero=validated_data["genero"],usuario=validated_data["usuario"])
        file = File(nombreDocumento = validated_data['nombreDocumento'],documento_file = validated_data['documento_file'])
        file.save()
        return file"""
    
class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        exclude = ('idPerfil',)