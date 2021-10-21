from authApp.models.product import Product
from rest_framework          import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['marca', 'modelo', 'stock', 'precio']

    def to_representation(self, obj):
        product = Product.objects.get(id=obj.id)
        
        return {
            'id'     : product.id,
            'marca'  : product.marca,
            'modelo' : product.modelo,
            'stock'  : product.stock,
            'precio' : product.precio
        }