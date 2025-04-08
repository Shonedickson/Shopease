from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings





urlpatterns = [
   #path('admin/', admin.site.urls),    
    path('customer_dashboard/',views.customer_dashboard,name='customer_dashboard'),  
    path('customer_profile/',views.customer_profile,name='customer_profile'), 
    path('customer_edit_data/<int:aid>/', views.customer_edit_data, name='customer_edit_data'),
    path('customer_update_data/', views.customer_update_data, name='customer_update_data'),
    path('merchants/',views.merchants,name='merchants'), 
    path('merchant_products/<int:mrhnt_id>/',views.merchant_products,name='merchant_products'), 
    path('home_products/',views.home_products,name='home_products'), 
    path('home_product_details/<int:ptid>/',views.home_product_details,name='home_product_details'), 
    path('delivery_address/<int:cstid>/',views.delivery_address,name='delivery_address'), 
    path('add_customer_registration/',views.add_customer_registration,name='add_customer_registration'), 
    path('add_cregistartion_save_data/',views.add_cregistartion_save_data,name='add_cregistartion_save_data'), 
    path('order/',views.order,name='order'),
    path('add_to_cart/',views.add_to_cart,name='add_to_cart'), 
    path('edit_quantity/<int:qid>/',views.edit_quantity,name='edit_quantity'), 
    path('update_quantity/', views.update_quantity, name='update_quantity'),
    path('productcart_delete_data/<int:did>/' ,views.productcart_delete_data,name='productcart_delete_data'),
    path('select_address/', views.select_address, name='select_address'),
    path('update_address/', views.update_address, name='update_address'), 
    path('save_dt/', views.save_dt, name='save_dt'),
    path('completed_order/', views.completed_order, name='completed_order'),
    path('display_completed_order/<int:mid>/' ,views.display_completed_order,name='display_completed_order'),
    path('payment/<int:oid>', views.payment, name='payment'),
    path('payment_save/', views.payment_save, name='payment_save'),
    path('change_password_customer/', views.change_password_customer, name='change_password_customer'),
    path('update_password_customer/', views.update_password_customer, name='update_password_customer'),

]


     