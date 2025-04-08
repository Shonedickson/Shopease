from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings





urlpatterns = [
   #path('admin/', admin.site.urls),    
    path('employee_dashboard/',views.employee_dashboard,name='employee_dashboard'),   
    path('employee_profile/',views.employee_profile,name='employee_profile'),
    path('employee/profile_edit/<int:wid>/', views.profile_edit, name='profile_edit'),
    path('profile_update_data/<int:employee_id>',views.profile_update_data,name='profile_update_data'), 
    path('my_orders/',views.my_orders,name='my_orders'), 
    path('order_details/<int:cid>',views.order_details,name='order_details'),
    path('complete_order/<int:order_id>',views.complete_order,name='complete_order'), 
    path('completed_orders/',views.completed_orders,name='completed_orders'), 
    path('completed_details/<int:did>',views.completed_details,name='completed_details'), 
    path('change_password_employee/', views.change_password_employee, name='change_password_employee'),
    path('update_password_employee/', views.update_password_employee, name='update_password_employee'),

]

