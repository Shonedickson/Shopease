from django.shortcuts import render,redirect
from newapp import models
from django.http import HttpResponse
import os
from django.contrib import messages



def employee_dashboard(request):
    return render(request,'employee_dashboard/employee_layout.html')

def employee_profile(request):

    uname = request.session['demail']
    
    udata = models.Employee.objects.get(email=uname)
    
    context = {'prof': udata}
    
    return render(request, 'employee_dashboard/employee_profile.html', context)
def profile_edit(request, wid):
    emp_data=models.Employee.objects.get(emp_id=wid)

    context = {'empdatadata': emp_data}
    return render(request, 'employee_dashboard/profile_edit.html', context)


def profile_update_data(request, employee_id):
    if request.method == 'POST':
        name = request.POST["name"]
        address = request.POST["address"]
        phone_number = request.POST["phone"]
        gender = request.POST["gender"]
        employee_id = request.POST["wid"]
        empdatadata = models.Employee.objects.get(emp_id=employee_id)
        empdatadata.name = name
        empdatadata.address = address
        empdatadata.phone_num = phone_number
        empdatadata.gender = gender
        empdatadata.save()
        return redirect('employee_profile')

def my_orders(request):
    employee_email = request.session.get('demail')
    customers = models.Customer.objects.filter(email_id=employee_email)
    orders = models.OrderTable.objects.filter(fk_cust_id__in=customers.values('cust_id'))
    context = {
        'clist': customers,
        'olist': orders
    }
    return render(request, 'employee_dashboard/my_orders.html', context)

def order_details(request,cid):    
    # Query for the order in 'progressed' status
    order = models.OrderTable.objects.filter(fk_cust_id=cid, order_status='scheduled').first()
    
    if order:
        order_id = order.order_id    

        # Count items
        item_query = """
                SELECT order_table.order_id, COUNT(*) AS item_count
                FROM order_table
                INNER JOIN order_lines ON order_table.order_id = order_lines.fk_order_id
                WHERE order_table.fk_cust_id=%s AND order_table.order_status='scheduled'
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
                WHERE order_table.fk_cust_id=%s AND order_table.order_status='scheduled'
            """
        cart_items = models.OrderTable.objects.raw(cart_items_query, [cid])
        print(cart_items)

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

    return render(request, 'employee_dashboard/order_details.html', context)
def complete_order(request,order_id):
    sdata=models.OrderTable.objects.get(order_id=order_id)
    sdata.order_status='completed'
    sdata.save()
    data=models.ScheduleEmployee.objects.get(fk_order_id=order_id)
    data.status='completed'
    data.save()
    return redirect('my_orders')

def completed_orders(request):    
    employee_email = request.session.get('demail')
    customers = models.Customer.objects.filter(email_id=employee_email)
    orders = models.OrderTable.objects.filter(
        fk_cust_id__in=customers.values('cust_id'),
        order_status='completed'
    )
    context = {
        'clist': customers,
        'olist': orders
    }

    return render(request, 'employee_dashboard/completed_orders.html', context)


def completed_details(request,did):    
 
    order = models.OrderTable.objects.filter(fk_cust_id=did, order_status='completed').first()
    
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
        item = models.OrderTable.objects.raw(item_query, [did])

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
        cart_items = models.OrderTable.objects.raw(cart_items_query, [did])
        print(cart_items)

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

    return render(request, 'employee_dashboard/completed_details.html', context)    



def change_password_employee(request):
	return render(request,"employee_dashboard/change_password.html")

def update_password_employee(request):
    npass = request.POST['npass']
    cpass = request.POST['cpass']
    uname = request.session['demail']
    
    if npass == cpass:
        log = models.Login.objects.get(username=uname)
        log.password = npass
        log.save()
        messages.success(request, "Password changed successfully!")
        return redirect("employee_dashboard") 
    else:
        messages.error(request, "Passwords do not match. Please try again.")
        return redirect("change_password_employee")





