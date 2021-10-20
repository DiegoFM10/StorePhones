from authApp.models.product import Product
#from authApp.models.user     import User
from rest_framework          import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['marca', 'modelo', 'stock', 'precio']

    def to_representation(self, obj):
        product = Product.objects.get(id=obj.id)
        #origin_account  = Account.objects.get(id=obj.origin_account_id)
        #destiny_account = Account.objects.get(id=obj.destiny_account_id)
        return {
            'id'     : product.id,
            'marca'  : product.marca,
            'modelo' : product.modelo,
            'stock'  : product.stock,
            'precio' : product.precio
        }