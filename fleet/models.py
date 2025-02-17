from django.conf import settings
from django.db import models
import datetime

# Customer Registration Form
class Customer_Registration(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Declined', 'Declined'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    registered_name = models.CharField(max_length=200)
    trading_name = models.CharField(max_length=200, null=True, blank=True)
    billing_address = models.CharField(max_length=200)
    customer_TIN = models.CharField(max_length=200)
    customer_VAT = models.CharField(max_length=200)
    email_address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.trading_name

# Products Form
class Products(models.Model):
        STATUS_CHOICES = [
            ('Pending', 'Pending'),
            ('Approved', 'Approved'),
            ('Declined', 'Declined'),
        ]
        status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
        product_name = models.CharField(max_length=200)
        product_description = models.CharField(max_length=200)
        UOM = models.CharField(max_length=200)  # Consider renaming to uom for consistency
        truck_type = models.CharField(max_length=200)

        def __str__(self):  # Use __str__ instead of _str_
            return self.product_name

# Route Form
class Route(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Declined', 'Declined'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    route_name = models.CharField(max_length=200)
    loading_point = models.CharField(max_length=200)
    offloading_point = models.CharField(max_length=200, null=True, blank=True)
    number_of_checkpoints = models.CharField(max_length=200)
    checkpoints = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.route_name


# Sales Order Form.
class Sales_Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Declined', 'Declined'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    date = models.DateField(default=datetime.datetime.today)
    customer = models.ForeignKey(Customer_Registration, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    UOM = models.CharField(max_length=200, null=True, blank=True)
    quantity = models.IntegerField(default=0)
    truck_type = models.CharField(max_length=200)
    number_of_trucks = models.IntegerField(default=0)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    number_of_trucks_remaining = models.IntegerField(default=0)
    number_of_trucks_allocated = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.customer} for {self.product}"


# Transporter Registration Form
class Transporter_Registration(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Declined', 'Declined'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    transporter_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.transporter_name


class Transporter_Order(models.Model):
    order_number = models.CharField(max_length=200)
    date = models.DateField(default=datetime.datetime.today)
    sales_order = models.ForeignKey(Sales_Order, on_delete=models.CASCADE, null=True)
    transporter = models.ForeignKey(Transporter_Registration, on_delete=models.CASCADE, null=True)
    driver = models.CharField(max_length=200)
    truck_reg_number = models.CharField(max_length=200)
    trailer1_reg_number = models.CharField(max_length=200)
    trailer2_reg_number = models.CharField(max_length=200)
    container_number = models.CharField(max_length=200)
    booking_ref = models.CharField(max_length=200)
    charge = models.CharField(max_length=200)
    charge_type = models.CharField(max_length=200)
    customer_invoice_number = models.CharField(max_length=200)
    POD_number = models.CharField(max_length=200, default=1, null=True, blank=True)
    status = models.CharField(max_length=200, default='Pending')
    route = models.ForeignKey(Route, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)

    def __str__(self):
        transporter_name = self.transporter.transporter_name if self.transporter else "No Transporter"
        route_name = self.route.route_name if self.route else "No Transporter"
        return f'{self.order_number} {self.sales_order} {transporter_name} {route_name}'

# Truck Type Form
class Truck_Type(models.Model):
    truck_type = models.CharField(max_length=200)
    load_tonnage = models.CharField(max_length=200)
    status = models.CharField(max_length=200, default='Pending')  # Add this line

    def _str_(self):
        return f'{self.truck_type} {self.load_tonnage}'

# Fuel Service Providers Form
class Fuel_Service_Providers(models.Model):
    registered_name = models.CharField(max_length=200)
    trading_name = models.CharField(max_length=200)
    billing_address = models.CharField(max_length=200)
    supplier_TIN = models.CharField(max_length=200)
    supplier_VAT = models.CharField(max_length=200)
    email_address = models.EmailField(max_length=200, null=True, blank=True)

    def _str_(self):
        return f'{self.registered_name} {self.trading_name}'


# Transporter Payment Form
class Transporter_Payment(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Declined', 'Declined'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    date = models.DateField(default=datetime.datetime.today)
    transporter = models.CharField(max_length=200)
    payment_type = models.CharField(max_length=200)
    source_ref = models.CharField(max_length=200)
    truck_reg_number = models.CharField(max_length=200)
    service_provider = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)
    unit_price = models.CharField(max_length=200)
    payment_amount = models.CharField(max_length=200)
    matched_orders = models.CharField(max_length=200)

    def _str_(self):
        return f'{self.transporter} {self.truck_reg_number} {self.payment_amount}'


# Generate Transporter Statement Form
class Transporter_Statement(models.Model):
    objects = None
    transporter_name = models.CharField(max_length=200)
    date_from = models.DateField(default=datetime.datetime.today)
    date_to = models.DateField(default=datetime.datetime.today)

    def _str_(self):
        return f'{self.transporter_name} {self.date_from} {self.date_to}'

    # Sign Up Model


class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('driver', 'Driver'),
        ('dispatcher', 'Dispatcher'),
        ('fleet_manager', 'Fleet Manager'),
    ]
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('suspended', 'Suspended'),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='driver')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return f"{self.user.username} - {self.role}"





