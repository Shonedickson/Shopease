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
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
   
    path('',views.home,name='home'),
    path('administrator/',include('administrator.urls')),
    path('merchant_registration',views.merchant_registration,name='merchant_registration'),
    path('mregistration_save_data/', views.mregistration_save_data,name='mregistration_save_data'),

    path('customerregistration',views.customerregistration,name='customerregistration'),
    path('cregistartion_save_data', views.cregistartion_save_data,name='cregistartion_save_data'),
    path('login', views.login,name='login'),
    path('check_login', views.check_login,name='check_login'),
    path('merchant/',include('merchant.urls')),  
    path('customer/',include('customer.urls')), 
    path('employee/',include('employee.urls')), 
     

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

