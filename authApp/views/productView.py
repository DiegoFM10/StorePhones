from django.conf                           import settings
from django.db.models import query
from django.db.models.query import QuerySet
from rest_framework                        import generics, status, views
from rest_framework import serializers
from rest_framework.response               import Response
from rest_framework.permissions            import IsAuthenticated
from rest_framework.serializers import Serializer
from rest_framework_simplejwt.backends     import TokenBackend

from authApp.models.product                import Product

from authApp.serializers.productSerializer import ProductSerializer



class TestView(views.APIView):
    def get(self, request):
        response = {"mensaje": "Esto es prueba"}
        return Response(data=response, status=status.HTTP_200_OK)

class ProductView(views.APIView):

    def get(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(data=queryset, many=True)  
        serializer.is_valid()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class ProductCreateView(views.APIView):
    def post(self, request):
        print("Información obtenida", request.data)
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()   
            data = {"message": "Se creó el producto"}
            return Response(data=data, status=status.HTTP_201_CREATED) 
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 

class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 


""" class ProductDetailView(generics.RetrieveAPIView):
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
        return super().destroy(request, *args, **kwargs) """