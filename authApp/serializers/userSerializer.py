from rest_framework import serializers
from authApp.models.user import User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['nombre', 'apellido', 'email', 'password', 'telefono']

    def create(self, validated_data):
        
        userInstance = User.objects.create(**validated_data)
       
        return userInstance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        return {
            'id': user.id,
            'nombre': user.nombre,
            'apellido': user.apellido,
            'email': user.email,
            'password': user.password,
            'telefono': user.telefono
        }