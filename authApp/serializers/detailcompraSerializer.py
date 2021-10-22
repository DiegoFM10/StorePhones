from django.db import models
from authApp.models.detailcompra  import DetailCompra
from rest_framework             import serializers

class detaCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailCompra
        fiels = {'User', 'Product', 'cantidad', 'valor_total'}

    def to_representation(self, obj):
        detaCompra = DetailCompra.objects.get(id=obj.id)

        return{
            'id          ' : detaCompra.id,
            'user        ' : detaCompra.user,   
            'product     ' : detaCompra.product,
            'cantidad    ' : detaCompra.cantidad,
            'valor_total ' : detaCompra.valor_total          
        } 