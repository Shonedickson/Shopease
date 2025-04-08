# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Area(models.Model):
    area_id = models.AutoField(primary_key=True)
    area_code = models.IntegerField()
    area_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'area'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bank(models.Model):
    bank_id = models.AutoField(primary_key=True)
    card_num = models.CharField(max_length=50)
    cvv_num = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=0)
    exp_month = models.CharField(max_length=20)
    exp_year = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'bank'


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50)
    category_image = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'category'


class Customer(models.Model):
    cust_id = models.AutoField(primary_key=True)
    cust_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    email_id = models.CharField(max_length=100)
    created_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'customer'


class CustomerAddress(models.Model):
    delivery_add_id = models.AutoField(primary_key=True)
    fk_cust_id = models.IntegerField()
    fk_area_id = models.IntegerField()
    street = models.CharField(max_length=50)
    building = models.CharField(max_length=100)
    flat = models.IntegerField()
    landmark = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'customer_address'


class DeliveryCharge(models.Model):
    delivery_charge_id = models.AutoField(primary_key=True)
    fk_area_id = models.IntegerField()
    delivery_charge = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'delivery_charge'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.TextField()
    phone_num = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    gender = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'employee'


class Login(models.Model):
    username = models.CharField(primary_key=True, max_length=100)
    password = models.CharField(max_length=20)
    user_type = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'login'


class Merchant(models.Model):
    merchant_id = models.AutoField(primary_key=True)
    merchant_name = models.CharField(max_length=50)
    address = models.TextField()
    phone_number = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'merchant'


class OrderLines(models.Model):
    order_line_id = models.AutoField(primary_key=True)
    fk_product_details_id = models.IntegerField()
    fk_order_id = models.IntegerField()
    quantity = models.IntegerField()
    sales_price = models.DecimalField(max_digits=10, decimal_places=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'order_lines'


class OrderTable(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateField(blank=True, null=True)
    fk_cust_id = models.IntegerField(blank=True, null=True)
    fk_delivery_address_id = models.IntegerField(blank=True, null=True)
    fk_merchant_id = models.IntegerField(blank=True, null=True)
    delivery_charge = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    net_amount = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    grand_total = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    order_status = models.CharField(max_length=50, blank=True, null=True)
    payment_mode = models.CharField(max_length=50, blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)
    delivered_time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_table'


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    fk_merchant_id = models.IntegerField()
    product_name = models.CharField(max_length=100)
    product_code = models.CharField(max_length=100)
    product_image = models.CharField(max_length=100)
    fk_sub_category_id = models.IntegerField()
    cost_price = models.DecimalField(max_digits=10, decimal_places=0)
    sales_price = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'product'


class ProductDetails(models.Model):
    product_details_id = models.AutoField(primary_key=True)
    fk_product_id = models.IntegerField()
    product_size = models.CharField(max_length=50)
    product_colour = models.CharField(max_length=50)
    product_img = models.CharField(max_length=100)
    product_quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_details'


class ScheduleEmployee(models.Model):
    sh_emp_id = models.AutoField(primary_key=True)
    fk_emp_id = models.IntegerField()
    fk_order_id = models.IntegerField()
    status = models.CharField(max_length=100)
    delivery_date = models.DateField()
    delivery_time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'schedule_employee'


class Subcategory(models.Model):
    sub_category_id = models.AutoField(primary_key=True)
    fk_category_id = models.IntegerField()
    category_type = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'subcategory'