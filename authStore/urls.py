from django.contrib import admin
from django.urls import path
#from authApp.views.productView import ProductDeleteView, ProductUpdateView, ProductDetailView, ProductCreateView, TestView, ProductView
#from authApp.views.productView import TestView, ProductView, ProductCreateView
from rest_framework_simplejwt.views    import TokenObtainPairView, TokenRefreshView
from authApp                           import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.TestView.as_view()),
    path('products/', views.ProductView.as_view()),
    path('product/add/', views.ProductCreateView.as_view()),
    path('productss/', views.ProductListCreateView.as_view()),
    path('product/<int:pk>', views.ProductRetrieveUpdateDestroy.as_view()),
    
    
]

