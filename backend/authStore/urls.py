from django.contrib import admin
from django.urls import path
from authApp.views.productView import ProductDeleteView, ProductUpdateView, ProductDetailView, ProductCreateView
from rest_framework_simplejwt.views    import TokenObtainPairView, TokenRefreshView
from authApp                           import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/',                 views.ProductCreateView.as_view()),
    path('product/<int:pk>/',        views.ProductDetailView.as_view()),
    path('product/update/<int:pk>/', views.ProductUpdateView.as_view()),
    path('product/remove/<int:pk>/', views.ProductDeleteView.as_view()),
]
