from django.shortcuts import render,redirect
from newapp import models
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password



# Create your views here.
def admin_dashboard(request):
    total_merchants = models.Merchant.objects.all()
    total_customers = models.Customer.objects.all()
    total_employees = models.Employee.objects.all()
    context = {
        'total_merchants': len(total_merchants), 
        'total_customers': len(total_customers),
        'total_employees': len(total_employees)
    }
    return render(request,'admin/admin.html',context)

def area(request):
    area=models.Area.objects.all()
    context={
        'alist':area
    }
    return render(request,'area/area.html',context)
def save_data(request):
    Areacode=request.POST["acode"]
    Areaname=request.POST["aname"]
      
    data=models.Area(area_code=Areacode,area_name=Areaname)
    data.save()
    


    return redirect('area')
def edit_data(request,aid):

    newdata=models.Area.objects.get(area_id=aid)
    context={
        'newdata':newdata

    }
    return render(request,'area/area_edit.html',context)
def update_data(request):
    Areacode=request.POST["acode"]
    Areaname=request.POST["aname"]
    area_id=request.POST["aid"]
    adata=models.Area.objects.get(area_id=area_id)
    adata.area_code=Areacode
    adata.area_name=Areaname
    
    adata.save()
    return redirect('area')  

def delete_data(request,aid):
    adata=models.Area.objects.get(area_id=aid)  
    adata.delete()
    return redirect('area')


def deliverycharge(request):
    deliverycharge=models.DeliveryCharge.objects.raw("SELECT * FROM area as a join delivery_charge as d on a.area_id=d.fk_area_id; ")
    area=models.Area.objects.all()
    context={
        'dlist':deliverycharge,
        'alist':area
    }
    return render(request,'delivery charge/deliverycharge.html',context)  

def deliverycharge_save_data(request):
    Area=request.POST["area"]
    DeliveryCharge=request.POST["dcharge"]
    
    
    data=models.DeliveryCharge(fk_area_id=Area,delivery_charge=DeliveryCharge)
    data.save()
    


    return redirect('deliverycharge')

def deliverycharge_edit_data(request,did):

    newdata=models.DeliveryCharge.objects.get(delivery_charge_id=did)
    area=models.Area.objects.all()
    context={
        'dlist':deliverycharge,
        'alist':area,
        'newdata':newdata

    }
    return render(request,'delivery charge/delivery_edit.html',context)   

def delivery_update_data(request):
    Area=request.POST["area"]
    DeliveryCharge=request.POST["dcharge"]
    delivery_charge_id=request.POST["did"]
    newdata=models.DeliveryCharge.objects.get(delivery_charge_id=delivery_charge_id)
    newdata.fk_area_id=Area
    newdata.delivery_charge=DeliveryCharge
    newdata.save()
    return redirect('deliverycharge')  
def delivery_delete_data(request,did):
    ddata=models.DeliveryCharge.objects.get(delivery_charge_id=did)  
    ddata.delete()
    return redirect('deliverycharge')





def category(request):
    category=models.Category.objects.all()
    context={
        'clist':category
    }
    return render(request,'category/category.html',context)  

def category_save_data(request):
    Categoryname=request.POST["cname"]
    Categoryimage=request.POST["cimage"]
    
    
    data=models.Category(category_name= Categoryname,category_image=Categoryimage)
    data.save()
    


    return redirect('category') 

def category_edit_data(request,cid):

    newdata=models.Category.objects.get(category_id=cid)
    context={
        'newdata':newdata

    }
    return render(request,'category/category_edit.html',context) 

def category_update_data(request):
    Categoryname=request.POST["cname"]
    Categoryimage=request.POST["cimage"]
    category_id=request.POST["cid"]
    cdata=models.Category.objects.get(category_id=category_id)
    cdata.category_name= Categoryname
    cdata.category_image=Categoryimage
    
    cdata.save()
    return redirect('category')              

def category_delete_data(request,cid):
    cdata=models.Category.objects.get(category_id=cid)  
    cdata.delete()
    return redirect('category')

def employee(request):
    employee=models.Employee.objects.all()
    context={
        'elist':employee
    }
    return render(request,'employee/employee.html',context)   


def employee_save_data(request):
    Name =request.POST["zname"]
    Address=request.POST["zaddress"]
    PhoneNumber=request.POST["zphone"]
    Email=request.POST["zemail"]
    Gender=request.POST["zgender"]
    Password=request.POST["zpassword"]
    
    
    data=models.Employee(name= Name,address= Address,phone_num=  PhoneNumber,email= Email,gender=Gender,)
    data.save()
    log = models.Login(
        username=Email,
        password=Password,
        user_type='employee',
        status='active'
    )
    log.save()

    


    return redirect('employee')      

def employee_edit_data(request,eid):

    newdata=models.Employee.objects.get(emp_id =eid)
    context={
        'newdata':newdata

    }
    return render(request,'employee/employee_edit.html',context) 

def employee_update_data(request):
    Name =request.POST["zname"]
    Address=request.POST["zaddress"]
    PhoneNumber=request.POST["zphone"]
    Email=request.POST["zemail"]
    Gender=request.POST["zgender"]
    employee_id=request.POST["eid"]
    edata=models.Employee.objects.get(emp_id=employee_id)
    edata.name= Name
    edata.address= Address
    edata.phone_num=PhoneNumber
    edata.email=Email
    edata.gender=Gender
    edata.save()
    return redirect('employee') 

def employee_delete_data(request,eid):
    edata=models.Employee.objects.get(emp_id=eid)  
    edata.delete()
    return redirect('employee')


def customer_details(request):
    customer = models.Customer.objects.all()
    context={
        'ulist':customer

    }
    return render(request, 'customer/customer_details.html', context)



def merchant_details(request):  
    inactive_merchants = models.Merchant.objects.filter(status='inactive')  
    return render(request, 'merchant/merchant_details.html', {'tlist': inactive_merchants})


def approve_merchant(request,mid):
    mdata=models.Merchant.objects.get(merchant_id=mid)
    mdata.status='active'
    mdata.save()
    Uname= mdata.email
    log=models.Login.objects.get(username=Uname)
    log.status='active'
    log.save()
    return redirect('merchant_details')



def reject_merchant(request, rid):
    mdata = models.Merchant.objects.get(merchant_id=rid)
    mdata.status = 'rejected'
    mdata.save()

    Uname = mdata.email
    log = models.Login.objects.get(username=Uname)
    log.status = 'rejected'
    log.save()
    return redirect('merchant_details') 


def new_merchant_details(request):

    merchant = models.Merchant.objects.filter(status='active')
    context = {
        'tlist': merchant
    }
    return render(request, 'newmerchant/approvedmerchants.html', context)





def new_rejected_merchant_details(request):

    merchant = models.Merchant.objects.filter(status='rejected')
    context = {
        'tlist': merchant
    }
    return render(request, 'newmerchant/rejectedmerchants.html', context)



def new_inactive_merchant_details(request):

    merchant = models.Merchant.objects.filter(status='inactive')
    context = {
        'tlist': merchant
    }
    return render(request, 'newmerchant/inactivemerchants.html', context)





def sub_category(request,cid):
    subcategory=models.Subcategory.objects.filter(fk_category_id=cid)
    context={
        'slist':subcategory,
        'cid':cid
    }
    return render(request,'category/subcategory.html',context)    



def sub_category_save_data(request):
    Categorytype=request.POST["ctype"]
    cat_id=request.POST['ctid']
   
    
    
    data=models.Subcategory(category_type= Categorytype,fk_category_id=cat_id)
    data.save()
    


    return redirect('sub_category',cid=cat_id) 

def sub_category_edit_data(request, kid):
    newdata = models.Subcategory.objects.get(sub_category_id=kid)
    context = {
        'newdata': newdata
    }
    return render(request, 'category/sub_category_edit.html', context)


def sub_category_update_data(request):
    category_type = request.POST.get("ctype")
    cat_id = request.POST.get("ctid")
        
    sdata=models.Subcategory.objects.get(sub_category_id=kid)
    sdata.category_type = category_type
    
            
    sdata.save()
    return redirect('sub_category', cid=cat_id)  


def display_orders(request):
    customers=models.OrderTable.objects.raw("SELECT * FROM customer as t join order_table as o on t.cust_id=o.fk_cust_id; ")
    
       
      

    context = {
        
        'tlist': customers,
    
        
    }
    return render(request, 'display_orders/display.html', context)
def display_orders_product(request, cid):
    # Query for the order in 'progressed' status
    order = models.OrderTable.objects.filter(fk_cust_id=cid, order_status='progressed').first()
    
    if order:
        order_id = order.order_id    

        # Count items
        item_query = """
                SELECT order_table.order_id, COUNT(*) AS item_count
                FROM order_table
                INNER JOIN order_lines ON order_table.order_id = order_lines.fk_order_id
                WHERE order_table.fk_cust_id=%s AND order_table.order_status='progressed'
                GROUP BY order_table.order_id 
            """
        item = models.OrderTable.objects.raw(item_query, [cid])

        # Get cart items and customer address with area details (join fk_delivery_address_id with delivery_add_id)
        cart_items_query = """
                SELECT order_table.order_id, 
                       order_lines.*, 
                       product_details.*, 
                       product.*, 
                       customer_address.*, 
                       area.area_name, 
                       area.area_code
                FROM order_table
                INNER JOIN order_lines ON order_table.order_id = order_lines.fk_order_id
                INNER JOIN product_details ON order_lines.fk_product_details_id = product_details.product_details_id
                INNER JOIN product ON product.product_id = product_details.fk_product_id
                INNER JOIN customer_address ON customer_address.delivery_add_id = order_table.fk_delivery_address_id
                INNER JOIN area ON area.area_id = customer_address.fk_area_id
                WHERE order_table.fk_cust_id=%s AND order_table.order_status='progressed'
            """
        cart_items = models.OrderTable.objects.raw(cart_items_query, [cid])

        # Calculate sum of total prices from cart items
        sum_total = sum(item.total_price for item in cart_items)

        context = {
            'ilist': item,
            'clist': cart_items,
            'sum_total': sum_total,
            'order_id': order_id,
        }
    else:
        order_id = None
        context = {
            'ilist': [],
            'clist': [],
            'sum_total': 0,
            'order_id': order_id,
        }

    return render(request, 'display_orders/display_product.html', context)



def employee_schedule(request,oid):   
    schedule=models.ScheduleEmployee.objects.raw("SELECT * FROM employee as e join schedule_employee as s on e.emp_id=s.fk_emp_id; ")
    employees = models.Employee.objects.all()  
    order=models.OrderTable.objects.all()
    
    context = {
        'elist': employees,
        'slist':  schedule,
        'olist': order,
        'oid':oid
    }
    
    return render(request, 'employee_schedule/employee_schedule.html', context)



def employee_schedule_save_data(request):
    employee=request.POST["e1"]
    ddate=request.POST["e2"]
    dtime=request.POST["e3"]
     
    oid = request.POST["e4"]

    order_status="scheduled"
  
    order = models.OrderTable.objects.get(order_id=oid)
    order.order_status=order_status
    order.save()

    data=models.ScheduleEmployee(fk_emp_id=employee, delivery_date=ddate,delivery_time=dtime,fk_order_id=oid,status='scheduled')
    data.save()



    return redirect(display_orders)  
    
def display_employee_details(request): 
    ordertable = models.OrderTable.objects.first()  
    scheduled_employee = models.ScheduleEmployee.objects.raw("""
        SELECT * FROM employee AS e 
        JOIN schedule_employee AS s ON e.emp_id = s.fk_emp_id
        WHERE s.fk_order_id = %s
    """, [ordertable.order_id])  
   
    employee = models.Employee.objects.all()

   
    context = {
        'elist': employee,
        'slist': scheduled_employee,
        'ordertable': ordertable
    }

    return render(request, 'employee_schedule/emplo_details.html', context)


def display_completed_orders(request, jid):

    order = models.OrderTable.objects.filter(fk_cust_id=jid, order_status='completed').first()
    
    if order:
        order_id = order.order_id    

        # Count items
        item_query = """
                SELECT order_table.order_id, COUNT(*) AS item_count
                FROM order_table
                INNER JOIN order_lines ON order_table.order_id = order_lines.fk_order_id
                WHERE order_table.fk_cust_id=%s AND order_table.order_status='completed'
                GROUP BY order_table.order_id 
            """
        item = models.OrderTable.objects.raw(item_query, [jid])

        # Get cart items and customer address with area details (join fk_delivery_address_id with delivery_add_id)
        cart_items_query = """
                SELECT order_table.order_id, 
                       order_lines.*, 
                       product_details.*, 
                       product.*, 
                       customer_address.*, 
                       area.area_name, 
                       area.area_code
                FROM order_table
                INNER JOIN order_lines ON order_table.order_id = order_lines.fk_order_id
                INNER JOIN product_details ON order_lines.fk_product_details_id = product_details.product_details_id
                INNER JOIN product ON product.product_id = product_details.fk_product_id
                INNER JOIN customer_address ON customer_address.delivery_add_id = order_table.fk_delivery_address_id
                INNER JOIN area ON area.area_id = customer_address.fk_area_id
                WHERE order_table.fk_cust_id=%s AND order_table.order_status='completed'
            """
        cart_items = models.OrderTable.objects.raw(cart_items_query, [jid])

        # Calculate sum of total prices from cart items
        sum_total = sum(item.total_price for item in cart_items)

        context = {
            'ilist': item,
            'clist': cart_items,
            'sum_total': sum_total,
            'order_id': order_id,
        }
    else:
        order_id = None
        context = {
            'ilist': [],
            'clist': [],
            'sum_total': 0,
            'order_id': order_id,
        }

    return render(request, 'display_orders/display_completed_orders.html', context)

    
def view_employee_details(request,oid):    
    ordertable = models.OrderTable.objects.get(order_id=oid) 
    scheduled_employee = models.ScheduleEmployee.objects.raw("""
        SELECT * FROM employee AS e 
        JOIN schedule_employee AS s ON e.emp_id = s.fk_emp_id
        WHERE s.fk_order_id = %s
    """, [oid])  
    employee = models.Employee.objects.all()

    context = {
        'elist': employee,
        'slist': scheduled_employee,
        'ordertable': ordertable  
    }

    return render(request, 'display_orders/employee_details.html', context)
    
def change_password(request):
	return render(request,"admin/change_password.html")

def update_password(request):
    npass = request.POST['npass']
    cpass = request.POST['cpass']
    uname = request.session['semail']
    
    if npass == cpass:
        log = models.Login.objects.get(username=uname)
        log.password = npass
        log.save()
        messages.success(request, "Password changed successfully!")
        return redirect("admin_dashboard") 
    else:
        messages.error(request, "Passwords do not match. Please try again.")
        return redirect("change_password")







