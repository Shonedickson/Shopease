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
     path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
     path('area/',views.area,name='area'),
     path('save_data/', views.save_data,name='save_data'),
     path('edit_data/<int:aid>/' ,views.edit_data,name='edit_data'),
     path('update_data/',views.update_data,name='update_data'),
     path('delete_data/<int:aid>/' ,views.delete_data,name='delete_data'),
     path('deliverycharge/',views.deliverycharge,name='deliverycharge'),
     path('deliverycharge_save_data/', views.deliverycharge_save_data,name='deliverycharge_save_data'),
     path('deliverycharge_edit_data/<int:did>/' ,views.deliverycharge_edit_data,name='deliverycharge_edit_data'),
     path('delivery_update_data/',views.delivery_update_data,name='delivery_update_data'),
     path('delivery_delete_data/<int:did>/' ,views.delivery_delete_data,name='delivery_delete_data'),
     path('category/',views.category,name='category'),
     path('category_save_data/', views.category_save_data,name='category_save_data'),
     path('category_edit_data/<int:cid>/' ,views.category_edit_data,name='category_edit_data'),
     path('category_update_data/',views.category_update_data,name='category_update_data'),
     path('category_delete_data/<int:cid>/' ,views.category_delete_data,name='category_delete_data'),
     path('employee/',views.employee,name='employee'),
     path('employee_save_data/', views.employee_save_data,name='employee_save_data'),
     path('employee_edit_data/<int:eid>/' ,views.employee_edit_data,name='employee_edit_data'),
     path('employee_update_data/',views.employee_update_data,name='employee_update_data'),
     path('employee_delete_data/<int:eid>/' ,views.employee_delete_data,name='employee_delete_data'),
     path('customer_details/', views.customer_details, name='customer_details'),
     path('merchant_details/', views.merchant_details, name='merchant_details'),  
     path('approve_merchant/<int:mid>/', views.approve_merchant, name='approve_merchant'),
     path('reject_merchant/<int:rid>/', views.reject_merchant, name='reject_merchant'),
     path('new_merchant_details/', views.new_merchant_details, name='new_merchant_details'),
     path('new_rejected_merchant_details/', views.new_rejected_merchant_details, name='new_rejected_merchant_details'),
     path('new_inactive_merchant_details/', views.new_inactive_merchant_details, name='new_inactive_merchant_details'),
     path('sub_category/<int:cid>/',views.sub_category,name='sub_category'),
     path('sub_category_save_data/', views.sub_category_save_data,name='sub_category_save_data'),
     path('sub_category_edit_data/<int:kid>/' ,views.sub_category_edit_data,name='sub_category_edit_data'),
     path('sub_category_update_data/',views.sub_category_update_data,name='sub_category_update_data'),
     path('display_orders/',views.display_orders,name='display_orders'),
     path('display_orders_product/<int:cid>',views.display_orders_product,name='display_orders_product'),
     path('employee_schedule/<int:oid>',views.employee_schedule,name='employee_schedule'),
     path('employee_schedule_save_data/',views.employee_schedule_save_data,name='employee_schedule_save_data'),
     path('display_employee_details/',views.display_employee_details,name='display_employee_details'),
     path('display_completed_orders/<int:jid>',views.display_completed_orders,name='display_completed_orders'),
     path('view_employee_details/<int:oid>',views.view_employee_details,name='view_employee_details'),
     path('change_password/', views.change_password, name='change_password'),
     path('update_password/', views.update_password, name='update_password'),
 
]



     



     


     



