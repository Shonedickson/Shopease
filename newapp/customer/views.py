from django.shortcuts import render,redirect
from newapp import models
from django.utils import timezone
from django.contrib import messages
from django.http import HttpResponse



# Create your views here.
def customer_dashboard(request):
    return render(request,'customer_dashboard/customer.html')
def customer_profile(request):
    lname = request.session['lemail'] 
    ldata = models.Customer.objects.get(email_id=lname)
    cstid = ldata.cust_id 
    
   
    customeraddress = models.CustomerAddress.objects.raw("""
        SELECT c.*, d.*, a.area_name 
        FROM customer AS c
        JOIN customer_address AS d ON c.cust_id = d.fk_cust_id
        JOIN area AS a ON d.fk_area_id = a.area_id
        WHERE d.fk_cust_id = %s
    """, [cstid])

    context = {
        'profile': ldata,
        'dlist': customeraddress
    }
    return render(request, 'customer_dashboard/customer_profile.html', context)

def customer_edit_data(request, aid):
    lname = request.session['lemail'] 
    ldata = models.Customer.objects.get(email_id=lname)
    newdata = models.Customer.objects.get(cust_id=aid)
    
    context = {        
        'newdata': newdata        
    }
    return render(request, 'customer_dashboard/customer_edit.html', context)


def customer_update_data(request):
    Customername=request.POST["cname"]
    Customernumber=request.POST["cnumber"]
    cust_id=request.POST["aid"]
    cdata=models.Customer.objects.get(cust_id=cust_id)
    cdata.cust_name = Customername
    cdata.phone_number=Customernumber
    cdata.save()
    return redirect('customer_dashboard')     



def merchants(request):
    mdata = models.Merchant.objects.all()

    context = {
        'merchant': mdata
    }
    return render(request, 'customer_dashboard/merchant_profile.html', context)

def merchant_products(request, mrhnt_id):    
    products =models.Product.objects.filter(fk_merchant_id=mrhnt_id)

    context = {
        'product': products
    }

    return render(request, 'customer_dashboard/merchant_product.html', context)

def home_products(request):
    pdata=models.Product.objects.all()
    context={
        'product': pdata
    }
    return render (request,'customer_dashboard/home_products.html',context)   

def home_product_details(request,ptid):
    productdetails=models.ProductDetails.objects.raw("SELECT * FROM product as m join product_details as p on m.product_id=p.fk_product_id where p.fk_product_id=%s",[ptid])
    product=models.Product.objects.all()
    lname = request.session['lemail'] 
    ldata = models.Customer.objects.get(email_id=lname)
    cid=ldata.cust_id
    context={
        'plist': productdetails,
        'mlist': product,
        'cid':cid
        
    }


    return render (request,'customer_dashboard/home_product_details.html',context) 
def delivery_address(request):
    cname = request.session['cname']
    cdata = models.Customer.objects.get(cust_name=cname)
    

    
    customer = models.Customer.objects.all()

    context = {
        'clist': cdata,
        
    }

    return render(request, 'customer_dashboard/customer_profile.html', context)
def add_customer_registration(request):
    customerregistration = models.CustomerAddress.objects.raw("SELECT * FROM area as a join customer_address as c on a.area_id=c.fk_area_id; ")
    area = models.Area.objects.all()
    customer = models.Customer.objects.get(email_id=request.session['lemail'])  # Assuming customer is logged in
    
    context = {
        'clist': customerregistration,
        'alist': area,
        'customer': customer  # Pass the customer to the template
    }

    return render(request, 'customer_dashboard/add_customer_details.html', context)

def add_cregistartion_save_data(request):
    Area = request.POST["carea"]
    Street = request.POST["cstreet"]
    HouseName = request.POST["chouse_name"]
    HouseNo = request.POST["chouse_no"]
    Landmark = request.POST["clandmark"]

    
    Cust_id = request.POST["cid"]


  
    customer = models.Customer.objects.get(cust_id=Cust_id)

    data = models.CustomerAddress(
        fk_cust_id=Cust_id, 
        fk_area_id=Area,
        street=Street,
        building=HouseName,
        flat=HouseNo,
        landmark=Landmark
    )
    data.save()

    
    return redirect('customer_profile')

def order(request):
    # Retrieve the logged-in user's email from session
    username = request.session.get('lemail')
    if not username:
        messages.error(request, "You must be logged in to place an order.")
        return redirect("login")  # Redirect to the login page if not logged in

    # Fetch order details from the form submission
    pd_id = request.POST.get('pdid')
    price = request.POST.get('price')
    quantity = int(request.POST.get('squantity'))
    merchant_id = request.POST.get('mid')
    total_price = quantity * float(price)
    order_date = timezone.now().date()

    # Fetch the customer object
    customer = models.Customer.objects.filter(email_id=username).first()
    if not customer:
        messages.error(request, "Customer not found.")
        return redirect("login")

    # Fetch the product details
    product = models.ProductDetails.objects.filter(pk=pd_id).first()
    if not product:
        messages.error(request, "Product not found.")
        return redirect("home_product_details", pid=pd_id)

    # Check if there is enough stock for the requested quantity
    if product.product_quantity < quantity:
        messages.error(request, "Insufficient stock")
        return redirect("home_product_details", pid=product.fk_product_id)

    # Check if the customer already has an ongoing order
    order_count = models.OrderTable.objects.filter(order_status='progressed', fk_cust_id=customer.cust_id).count()

    if order_count == 0:
        # If no ongoing order exists, create a new order
        order = models.OrderTable.objects.create(
            order_date=order_date,
            fk_cust_id=customer.cust_id,
            fk_merchant_id=merchant_id,
            order_status='progressed'
        )
        order_id = order.order_id
        models.OrderLines.objects.create(
            fk_product_details_id=pd_id,
            fk_order_id=order_id,
            quantity=quantity,
            sales_price=price,
            total_price=total_price
        )
    else:
        # If an order exists, update the existing order
        order = models.OrderTable.objects.filter(fk_cust_id=customer.cust_id).latest('order_id')
        order_line = models.OrderLines.objects.filter(fk_order_id=order.order_id, fk_product_details_id=pd_id).first()

        if order_line is None:
            # If the product is not in the order yet, add a new order line
            models.OrderLines.objects.create(
                fk_product_details_id=pd_id,
                fk_order_id=order.order_id,
                quantity=quantity,
                sales_price=price,
                total_price=total_price
            )
        else:
            # If the product is already in the order, update the quantity and price
            new_quantity = order_line.quantity + quantity
            if product.product_quantity < new_quantity:
                messages.error(request, "Insufficient stock for updated quantity.")
                return redirect("add_to_cart")

            total = order_line.sales_price * new_quantity
            order_line.quantity = new_quantity
            order_line.total_price = total
            order_line.save()

    # Deduct the purchased quantity from the product's stock
    product.product_quantity -= quantity
    product.save()

    return redirect("add_to_cart") 
def add_to_cart(request):
    uname = request.session.get('lemail')
    if uname:
        cust = models.Customer.objects.get(email_id=uname)
        cid = cust.cust_id 
        order = models.OrderTable.objects.filter(fk_cust_id=cid, order_status='progressed').first()
        if order:
            order_id = order.order_id    
            item_query = """
                SELECT order_table.order_id, COUNT(*) AS item_count
                FROM order_table
                INNER JOIN order_lines ON order_table.order_id = order_lines.fk_order_id
                WHERE order_table.fk_cust_id=%s AND order_table.order_status='progressed'
                GROUP BY order_table.order_id
            """
            item = models.OrderTable.objects.raw(item_query, [cid])

            cart_items_query = """
                SELECT * FROM order_table 
                INNER JOIN order_lines ON order_table.order_id=order_lines.fk_order_id
                INNER JOIN product_details ON order_lines.fk_product_details_id=product_details.product_details_id
                INNER JOIN product ON product.product_id=product_details.fk_product_id      

                WHERE order_table.fk_cust_id=%s AND order_table.order_status='progressed'
            """
            cart_items = models.OrderTable.objects.raw(cart_items_query, [cid])

            sum_total = sum(item.total_price for item in cart_items)

            context = {
                'ilist': item,
                'clist': cart_items,
                'sum_total': sum_total,
                'order_id': order_id
            }
        else:
            order_id = None
            context = {
                'ilist': [],
                'clist': [],
                'sum_total': 0,
                'order_id': order_id
            }
   

    return render(request, 'customer_dashboard/add_to_cart.html', context)

def edit_quantity(request,qid):
    newquantity=models.OrderLines.objects.get(order_line_id=qid)
    context={
        'newquantity':newquantity
    }
    return render(request,'customer_dashboard/edit_quantity.html',context)

def update_quantity(request):
    Quantity = int(request.POST.get('squantity'))
    price = request.POST.get('sprice')
    order_id = request.POST.get("olid")
    Total_price = Quantity * float(price)
        
    odata=models.OrderLines.objects.get(order_line_id=order_id)
    odata.quantity = Quantity
    odata.sales_price = price
    odata.total_price = Total_price

    
            
    odata.save()
    return redirect('add_to_cart')   


def productcart_delete_data(request,did):
    odata=models.OrderLines.objects.get(order_line_id=did)  
    odata.delete()
    return redirect('add_to_cart')
def select_address(request):
    customer = models.Customer.objects.get(email_id=request.session.get('lemail')) 
    daddress = models.CustomerAddress.objects.raw(
        "SELECT * FROM area as a "
        "JOIN customer_address as c ON a.area_id = c.fk_area_id "
        "WHERE c.fk_cust_id = %s", [customer.cust_id]
    )
   
    product = models.Product.objects.all() 
    area = models.Area.objects.all()

    context = {
        'dlist': daddress,
        'alist': area,
        'customer': customer
    }

    return render(request, 'customer_dashboard/select_address.html', context)
def update_address(request):

    customer = models.Customer.objects.get(email_id=request.session.get('lemail'))
    delivery_add_id = request.POST.get('delivery_add_id')
    customer_address = models.CustomerAddress.objects.get(fk_cust_id=customer.cust_id, delivery_add_id=delivery_add_id)
    order = models.OrderTable.objects.get(fk_cust_id=customer.cust_id)
    dcharge = models.DeliveryCharge.objects.filter(fk_area_id=customer_address.fk_area_id).first()
    lorder = models.OrderLines.objects.filter(fk_order_id=order.order_id).first()
    
    order.net_amount = lorder.total_price if lorder else 0
    order.delivery_charge = dcharge.delivery_charge
    order.fk_delivery_address_id = customer_address.delivery_add_id
    order.grand_total = order.net_amount + order.delivery_charge
    
    order.save()

   
    messages.success(request, "Address and delivery charge updated successfully.")

    context = {
        'oid': order.order_id, 
        'dcharge': dcharge.delivery_charge,
    }

    return render(request, 'customer_dashboard/date_and_time.html', context)


def save_dt(request):
   
    Delivery_date = request.POST["ddate"]
    Delivery_time = request.POST["dtime"]
    oid = request.POST["order_id"]
    order = models.OrderTable.objects.get(order_id=oid) 
    dcharge = models.DeliveryCharge.objects.all()
    lorder = models.OrderLines.objects.all()


    order.delivery_date = Delivery_date
    order.delivered_time = Delivery_time
    order.save()

    return redirect('add_to_cart')


def completed_order(request):    
    customer_email = request.session.get('lemail')
    customers = models.Customer.objects.filter(email_id=customer_email)
    orders = models.OrderTable.objects.filter(
        fk_cust_id__in=customers.values('cust_id'),
        order_status='completed'
    )
    context = {
        'clist': customers,
        'olist': orders
    }

    return render(request, 'customer_dashboard/customer_details.html', context)    


def display_completed_order(request, mid):

    order = models.OrderTable.objects.filter(fk_cust_id=mid, order_status='completed').first()
    
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
        item = models.OrderTable.objects.raw(item_query, [mid])

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
        cart_items = models.OrderTable.objects.raw(cart_items_query, [mid])

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

    return render(request, 'customer_dashboard/display_completed_orders.html', context)   


def payment(request,oid):    

    grand_total_value = 0  
    order_id_value = None 

    orders = models.OrderTable.objects.raw(
        "SELECT o.*, c.*, o.grand_total, o.order_id FROM order_table o INNER JOIN customer c ON o.fk_cust_id = c.cust_id where o.order_id=%s",[oid])

 
    for order in orders:
        grand_total_value = order.grand_total  
        order_id_value = order.order_id  
        break 

    context = {
        'grand_total': grand_total_value,
        'oid': order_id_value        
    }

    
    return render(request,'customer_dashboard/payment.html',context)

def payment_save(request):
    card_num = request.POST['cardno']
    exp_month = request.POST['expmonth']
    exp_year = request.POST['expyear']
    cvv = request.POST['cvv']
    amount = float(request.POST['amount']) 
    order_id = request.POST['order_id'] 
    # print(order_id)

    bank_data = models.Bank.objects.get(cvv_num=cvv, exp_month=exp_month, exp_year=exp_year, card_num=card_num)


    if amount <= float(bank_data.amount):
        newamt = float(bank_data.amount) - amount 
        order_data = models.OrderTable.objects.get(order_id=order_id)
        order_data.order_status = 'paid'
        order_data.save()
        
        bank_data.amount = newamt
        bank_data.save()
        customer_id=order_data.fk_cust_id
        ordered_data = models.OrderTable.objects.raw(
        "SELECT * FROM order_table "
        "INNER JOIN order_lines ON order_table.order_id = order_lines.fk_order_id "
        "INNER JOIN product ON product.product_id = order_lines.fk_product_details_id "
        "WHERE order_table.fk_cust_id = %s "
        "AND order_table.order_status = 'paid' "
        "AND order_table.order_id = %s",
        [customer_id, order_id]
        )

        customer_data=models.Customer.objects.get(cust_id=customer_id)
        cart_data=models.OrderTable.objects.get(order_id=order_id)
        context={
        'olist':ordered_data,
        'cdata':customer_data,
        'cadata':cart_data
        }
        return render(request, "customer_dashboard/payment_done.html",context)
    else:
        return HttpResponse("Insufficient funds")    



def change_password_customer(request):
	return render(request,"customer_dashboard/change_password.html")

def update_password_customer(request):
    npass = request.POST['npass']
    cpass = request.POST['cpass']
    uname = request.session['lemail']
    
    if npass == cpass:
        log = models.Login.objects.get(username=uname)
        log.password = npass
        log.save()
        messages.success(request, "Password changed successfully!")
        return redirect("customer_dashboard") 
    else:
        messages.error(request, "Passwords do not match. Please try again.")
        return redirect("change_password_customer")




 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 