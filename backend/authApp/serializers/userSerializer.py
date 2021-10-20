from rest_framework import serializers
from authApp.models.user import User

class UserSerializer(serializers.ModelSerializer):
    # account = AccountSerializer()
    class Meta:
        model = User
        fields = ['id','nombre', 'apellido', 'email', 'password', 'telefono']

    def create(self, validated_data):
        # accountData = validated_data.pop('account')
        userInstance = User.objects.create(**validated_data)
        # Account.objects.create(user=userInstance, **accountData)
        return userInstance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        # account = Account.objects.get(user=obj.id)
        return {
            'id': user.id,
            'nombre': user.nombre,
            'apellido': user.apellido,
            'email': user.email,
            'password': user.password,
            'telefono': user.telefono
        }