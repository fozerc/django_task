"""
URL configuration for djangoProject1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shop_app.views import Register, UserLogin, UserLogout, AllProductsTemplate, \
    ProductViewingReturns, ProductsCreateView, ProductsUpdateView, ProductsListView, MainTemplate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', Register.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('check_products/', AllProductsTemplate.as_view(), name='check_products'),
    path('add_products/', ProductsCreateView.as_view(), name='add_product'),
    path('returns_products/', ProductViewingReturns.as_view(), name='check_returns'),
    path('update_products/<int:pk>', ProductsUpdateView.as_view(), name='update_product'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('', MainTemplate.as_view(), name='main'),

]
