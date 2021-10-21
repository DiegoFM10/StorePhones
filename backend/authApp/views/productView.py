from django.conf                           import settings
from rest_framework                        import generics, status
from rest_framework.response               import Response
from rest_framework.permissions            import IsAuthenticated
from rest_framework_simplejwt.backends     import TokenBackend

from authApp.models.product                import Product
#from authApp.models.account               import Account
from authApp.serializers.productSerializer import ProductSerializer

class ProductDetailView(generics.RetrieveAPIView):
    queryset           = Product.objects.all()
    serializer_class   = ProductSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        return super().get(request, *args, **kwargs)



class ProductCreateView(generics.CreateAPIView):
    serializer_class   = ProductSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        token        = self.request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != request.data['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response("Producto creado exitosamente", status=status.HTTP_201_CREATED)



class ProductUpdateView(generics.UpdateAPIView):
    queryset           = Product.objects.all()
    serializer_class   = ProductSerializer
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().update(request, *args, **kwargs)



class ProductDeleteView(generics.DestroyAPIView):
    queryset           = Product.objects.all()
    serializer_class   = ProductSerializer
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        token        = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data   = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().destroy(request, *args, **kwargs)