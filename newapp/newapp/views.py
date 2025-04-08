from django.shortcuts import render,redirect
from newapp  import models
from django.utils import timezone

import os
from django.core.files.storage import default_storage
from django.shortcuts import get_object_or_404
from django.contrib import messages


def home(request):
    return render(request,'home/home.html')


def merchant_registration(request):
    return render(request,'registration/registration.html')


def mregistration_save_data(request):
    Name = request.POST["mname"]
    Address = request.POST["maddress"]
    PhoneNumber = request.POST["mphn"]
    Email = request.POST["memail"]
    Password = request.POST["mpassword"]
    product_image = request.FILES.get('mimage')  
   
    image_path = None
    
    if product_image:
        image_name = product_image.name
        image_path = os.path.join('Merchant', image_name)  # Save the image in 'products' folder
        with default_storage.open(image_path, 'wb') as destination:
            for chunk in product_image.chunks():
                destination.write(chunk)
    
    # Saving merchant data
    data = models.Merchant(
        merchant_name=Name,
        address=Address,
        phone_number=PhoneNumber,
        email=Email,
        image=image_path,  
        status='inactive'
    )
    data.save()

    # Saving login data
    log = models.Login(
        username=Email,
        password=Password,
        user_type='merchant',
        status='inactive'
    )
    log.save()

    return redirect('home')

def customerregistration(request):
    customerregistration=models.CustomerAddress.objects.raw("SELECT * FROM area as a join customer_address as c on a.area_id=c.fk_area_id; ")
    area=models.Area.objects.all()
    context={
        'clist':customerregistration,
        'alist':area
        }



    return render(request,'registration/customerregistration.html',context)



def cregistartion_save_data(request):
    Name = request.POST["cname"]
    Phone = request.POST["cphone"]
    Email = request.POST["cemail"]
    cdate=timezone.now()

    Area = request.POST["carea"]
    Street = request.POST["cstreet"]
    HouseName = request.POST["chouse_name"]
    HouseNo = request.POST["chouse_no"]
    Landmark = request.POST["clandmark"]
    Password = request.POST["cpassword"]
    
    data=models.Customer( cust_name= Name,phone_number= Phone, email_id=Email,  created_date=  cdate)

    data.save()
    cust_id=data.cust_id

    data=models.CustomerAddress(fk_cust_id=cust_id,  fk_area_id= Area, street=  Street,  building= HouseName ,  flat=  HouseNo, landmark =Landmark)
    data.save()
    log=models.Login(username= Email,password= Password, user_type= 'customer',status= 'active' )
    log.save()
    
    


    return redirect('home')   


def login(request):
    return render (request,'login/login.html')    
def check_login(request): 
    if request.method == 'POST':
        uname = request.POST['email']
        password = request.POST['password']
        log_info = models.Login.objects.filter(username=uname,password =password)

        if log_info.exists():
            for log in log_info:
                if log.username == uname and log.password == password:
                    if log.user_type == 'admin' and log.status == 'active':
                        request.session['semail'] = log.username
                        return redirect("../administrator/admin_dashboard")

                    elif log.user_type == 'merchant' and log.status == 'active':
                        request.session['semail'] = log.username
                        return redirect("../merchant/merchant_dashboard")
                    elif log.user_type == 'customer' and log.status == 'active':
                        request.session['lemail'] = log.username
                        return redirect("../customer/customer_dashboard")
                    elif log.user_type == 'employee' and log.status == 'active':
                        request.session['demail'] = log.username
                        return redirect("../employee/employee_dashboard")


        # If the login does not exist or user is inactive, redirect to the login page
         return redirect('login')
    else:
        return redirect('login')






