from django.shortcuts import render,redirect
from newapp import models
from django.http import HttpResponse
import os
from django.core.files.storage import default_storage
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseBadRequest


def merchant_dashboard(request):
    return render(request,'merchant_dashboard/merchant_layout.html')

def merchant_profile(request):
    uname = request.session['semail']
    udata = models.Merchant.objects.get(email=uname)

    image_path = None
   
    product_image = request.FILES.get('product_image')  

    if product_image:
        image_name = product_image.name
        image_path = os.path.join('products', image_name)
        with default_storage.open(image_path, 'wb') as destination:
            for chunk in product_image.chunks():
                destination.write(chunk)

    context = {
        'profile': udata
    }
    return render(request, 'merchant_dashboard/merchant_profile.html', context)


def product(request):
    product=models.Product.objects.raw("SELECT * FROM Subcategory as s join product as p on s.sub_category_id=p.fk_sub_category_id; ")
    subcategory=models.Subcategory.objects.all()
    context={
        'plist':product,
        'slist':subcategory
    }
    return render(request, 'product/product.html', context)

def add_product(request):
    subcategory=models.Subcategory.objects.all()
    context={
        'slist':subcategory
    }
    return render(request, 'product/addproduct.html', context)

def product_save_data(request):
    if request.method == 'POST':
       
        uname = request.session['semail']
        merchant = models.Merchant.objects.get(email=uname)
        mid = merchant.merchant_id
        
       
        product_name = request.POST['pname']
        product_code = request.POST['pcode']
        product_image = request.FILES.get('pimage')  
        category = request.POST['pcategory']
        cost_price = request.POST['pcost']
        sales_price = request.POST['psales']
        
        
        image_path = None
        if product_image:
            image_name = product_image.name
            image_path = os.path.join('products', image_name)
            with default_storage.open(image_path, 'wb') as destination:
                for chunk in product_image.chunks():
                    destination.write(chunk)
        
       
        newdata = models.Product(
            product_name=product_name,
            product_code=product_code,
            product_image=image_path,  
            fk_sub_category_id=category,  
            cost_price=cost_price,
            sales_price=sales_price,
            fk_merchant_id=mid
        )
        newdata.save()
        
   
        return redirect("product") 

def product_edit_data(request, pid):
    newdata = models.Product.objects.get(product_id=pid)
    subcategory = models.Subcategory.objects.all()

    
    context = {
        'plist': product,  
        'slist': subcategory,
        'newdata': newdata  
    }
    return render(request, 'product/product_edit.html', context)


   



def product_delete_data(request, pid):
    
    product = models.Product.objects.get(product_id=pid)
    productdetails = models.ProductDetails.objects.filter(fk_product_id=pid).count()

    if productdetails == 0:
        product.delete()
        messages.success(request, "Product details deleted successfully!!!")
    else:
        messages.warning(request, "Cannot delete, product exists.")

    return redirect("product")


   
def product_update_data(request):
    Pname = request.POST["pname"]
    Pcode = request.POST["pcode"]  
    Pcost = request.POST["pcost"]
    Psales = request.POST["psales"]
    fk_sub_category_id = request.POST["pcategory"] 
    prt_id = request.POST['pid']
    
    ddata = models.Product.objects.get(product_id=prt_id)
    ddata.product_name = Pname
    ddata.product_code = Pcode
    ddata.cost_price = Pcost
    ddata.sales_price = Psales
    ddata.fk_sub_category_id = fk_sub_category_id

    ddata.save()

    return redirect('product')
  
def product_details(request,xid):
    product_details=models.ProductDetails.objects.filter(fk_product_id=xid)
    context = {
        'plist': product_details,
        'xid':xid
    }
    return render(request, 'product/product_details.html', context)


def productdetails_save_data(request):
    if request.method == 'POST':
        Product_size = request.POST["psize"]
        Product_colour = request.POST["pcolour"]
        Product_image = request.FILES.get('pimage')
        Product_quantity = request.POST["pquantity"]
        pdt_id=request.POST['ptid']


           
        image_path = None
        if Product_image:
            image_name = Product_image.name
            image_path = os.path.join('products', image_name)
            with default_storage.open(image_path, 'wb+') as destination:
                for chunk in Product_image.chunks():
                    destination.write(chunk)
        data = models.ProductDetails(
        fk_product_id=pdt_id,
        product_size=Product_size,
        product_colour=Product_colour,
        product_img=image_path,
        product_quantity=Product_quantity)
        data.save()
        return redirect('product_details',xid=pdt_id)



def productdetails_edit_data(request, xid):
    newdata = models.ProductDetails.objects.get(product_details_id=xid)      
    context = {
        'plist': product,          
        'newdata': newdata  
    }

    return render(request, 'product/productdetails_edit.html', context)    



def productdetails_update_data(request):
    Product_size = request.POST["psize"]
    Product_colour = request.POST["pcolour"]    
    Product_quantity = request.POST["pquantity"]
    pdt_id=request.POST['ptid']
    pdata=models.ProductDetails.objects.get(product_details_id =pdt_id)
    pdata.product_size=  Product_size
    pdata.product_colour = Product_colour 
    pdata.product_quantity=Product_quantity    
    pdata.save()
    return redirect('product')      


def productdetails_delete_data(request,xid):
    data=models.ProductDetails.objects.get(product_details_id=xid)  
    data.delete()
    return redirect('product') 

def product_change_image(request,prdct_id):
	Product=models.Product.objects.get(product_id =prdct_id)
	context={
	'product':Product
	}
	return render(request,"product/product_change_image.html",context)


def product_edit_image(request):
    if request.method == 'POST':
        prdct_id = request.POST.get('mmm') 
        image = request.FILES.get('pimage')  
        print(image)

        if prdct_id and image:
            try:
                product = models.Product.objects.get(product_id=prdct_id)
                image_name = image.name
                image_path = default_storage.save(f'products/{image_name}', image) 
                
                product.product_image = image_path  
                product.save()
                return redirect('product')  # Ensure this URL name is correct

            except Product.DoesNotExist:
                return redirect('product')

        # Handle missing prdct_id or image
        return HttpResponseBadRequest("Product ID or image missing.")
    
    # Handle non-POST requests
    return HttpResponse("Invalid request method.", status=405)


def merchant_change_image(request,mrhnt_id):
	merchant=models.Merchant.objects.get(merchant_id =mrhnt_id)
	context={
	'merchant':merchant
	}
	return render(request,"merchant_dashboard/merchant_change_image.html",context)    


def merchant_edit_image(request):
    if request.method == 'POST':
        mrhnt_id = request.POST.get('hhh')  
        image = request.FILES.get('mimage') 
        print(image)

        if mrhnt_id and image:
            try:
                
                merchant = models.Merchant.objects.get(merchant_id=mrhnt_id)
                
              
                image_name = image.name
                image_path = default_storage.save(f'Merchant/{image_name}', image) 

                # Update the merchant's image field (assuming `merchant.image` exists)
                merchant.image = image_path  
                merchant.save()

                # Redirect to the merchant dashboard or another relevant page
                return redirect('merchant_profile')  

            except merchant.DoesNotExist:
                # Merchant with the given ID does not exist
                return redirect('merchant_profile')

        # Handle missing mrhnt_id or image
        return HttpResponseBadRequest("Merchant ID or image missing.")
    
    # Handle non-POST requests
    return HttpResponse("Invalid request method.", status=405)

def change_password_merchant(request):
	return render(request,"merchant_dashboard/change_password.html")

def update_password_merchant(request):
    npass = request.POST['npass']
    cpass = request.POST['cpass']
    uname = request.session['semail']
    
    if npass == cpass:
        log = models.Login.objects.get(username=uname)
        log.password = npass
        log.save()
        messages.success(request, "Password changed successfully!")
        return redirect("merchant_dashboard") 
    else:
        messages.error(request, "Passwords do not match. Please try again.")
        return redirect("change_password_merchant")


