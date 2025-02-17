from django.contrib import admin
from .models import Sales_Order, Customer_Registration, Products, Transporter_Registration, Truck_Type, Route, \
    Fuel_Service_Providers, Transporter_Order, Transporter_Payment, Transporter_Statement

# Register your models here.


@admin.register(Sales_Order)
class Sales_OrderAdmin(admin.ModelAdmin):
    list_display = ('date', 'customer', 'product', 'quantity', 'UOM', 'truck_type',
                    'number_of_trucks', 'route')
    ordering = ('customer', 'product')
    search_fields = ('customer', 'product')


@admin.register(Customer_Registration)
class Customer_RegistrationAdmin(admin.ModelAdmin):
    list_display = ('trading_name', 'billing_address', 'customer_TIN', 'customer_VAT')
    ordering = ('trading_name', 'billing_address')
    search_fields = ('trading_name', 'billing_address')


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_description', 'UOM', 'truck_type')
    ordering = ('product_name', 'product_description')
    search_fields = ('product_name', 'product_description')


@admin.register(Transporter_Registration)
class Transporter_RegistrationAdmin(admin.ModelAdmin):
    list_display = ('transporter_name', 'address')
    ordering = ('transporter_name', 'address')
    search_fields = ('transporter_name', 'address')


@admin.register(Truck_Type)
class Truck_TypeAdmin(admin.ModelAdmin):
    list_display = ('truck_type', 'load_tonnage')
    ordering = ('truck_type', 'load_tonnage')
    search_fields = ('truck_type', 'load_tonnage')


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('route_name', 'loading_point', 'offloading_point', 'number_of_checkpoints',
                    'checkpoints')
    ordering = ('route_name', 'loading_point')
    search_fields = ('route_name', 'loading_point')


@admin.register(Fuel_Service_Providers)
class Fuel_Service_ProvidersAdmin(admin.ModelAdmin):
    list_display = ('registered_name', 'trading_name', 'billing_address', 'supplier_TIN',
                    'supplier_VAT')
    ordering = ('registered_name', 'trading_name', 'billing_address')
    search_fields = ('registered_name', 'trading_name')


@admin.register(Transporter_Order)
class Transporter_OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'date', 'sales_order', 'transporter', 'driver', 'truck_reg_number',
                    'trailer1_reg_number', 'trailer2_reg_number', 'container_number', 'booking_ref', 'route', 'product',
                    'charge', 'charge_type', 'customer_invoice_number')
    ordering = ('order_number', 'date', 'sales_order')
    search_fields = ('order_number', 'date', 'sales_order')


@admin.register(Transporter_Payment)
class Transporter_PaymentAdmin(admin.ModelAdmin):
    list_display = ('date', 'transporter', 'payment_type', 'source_ref',
                    'service_provider', 'quantity', 'unit_price', 'payment_amount', 'matched_orders')
    ordering = ('date', 'transporter')
    search_fields = ('transporter', 'payment_amount')


@admin.register(Transporter_Statement)
class Transporter_StatementAdmin(admin.ModelAdmin):
    list_display = ('transporter_name', 'date_from', 'date_to')
    ordering = ('transporter_name', 'date_from', 'date_to')
    search_fields = ('transporter_name', 'date_from', 'date_to')