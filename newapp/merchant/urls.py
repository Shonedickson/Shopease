"""
URL configuration for newapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views
from django.conf.urls.static import static
from django.conf import settings





urlpatterns = [
   #path('admin/', admin.site.urls),    
    path('merchant_dashboard/',views.merchant_dashboard,name='merchant_dashboard'),   
    path('merchant_profile/',views.merchant_profile,name='merchant_profile'),     
    path('product/',views.product,name='product'),  
    path('add_product/',views.add_product,name='add_product'),  
    path('product_save_data/', views.product_save_data, name='product_save_data'),
    path('product_edit_data/<int:pid>/', views.product_edit_data, name='product_edit_data'),
    path('product_delete_data/<int:pid>/', views.product_delete_data, name='product_delete_data'),
    path('product_update_data/', views.product_update_data, name='product_update_data'),
    path('product_details/<int:xid>//',views.product_details,name='product_details'),  
    path('productdetails_save_data/', views.productdetails_save_data, name='productdetails_save_data'),
    path('productdetails_edit_data/<int:xid>/', views.productdetails_edit_data, name='productdetails_edit_data'),
    path('productdetails_delete_data/<int:xid>/', views.productdetails_delete_data, name='productdetails_delete_data'),
    path('productdetails_update_data/', views.productdetails_update_data, name='productdetails_update_data'),
    path('product_change_image/<int:prdct_id>/', views.product_change_image, name='product_change_image'),
    path('product_edit_image/', views.product_edit_image, name='product_edit_image'),
    path('merchant_change_image/<int:mrhnt_id>/', views.merchant_change_image, name='merchant_change_image'),
    path('merchant_edit_image/', views.merchant_edit_image, name='merchant_edit_image'),
    path('change_password_merchant/', views.change_password_merchant, name='change_password_merchant'),
    path('update_password_merchant/', views.update_password_merchant, name='update_password_merchant'),

]

   
