from django import forms
from django.contrib.auth.models import User

from .models import Sales_Order, Customer_Registration, Route, Transporter_Registration, Truck_Type, Products, \
    Fuel_Service_Providers, Transporter_Order, Transporter_Payment, Transporter_Statement, UserProfile


class Sales_OrderForm(forms.ModelForm):
    class Meta:
        model = Sales_Order
        fields = ['date', 'customer', 'product', 'quantity', 'UOM', 'truck_type',
                  'number_of_trucks', 'route']


class Customer_RegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer_Registration
        fields = ['registered_name', 'trading_name', 'billing_address', 'customer_TIN',
                  'customer_VAT', 'email_address']


class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['route_name', 'loading_point', 'offloading_point', 'number_of_checkpoints', 'checkpoints']


class Transporter_RegistrationForm(forms.ModelForm):
    class Meta:
        model = Transporter_Registration
        fields = ['transporter_name', 'address']


class Truck_TypeForm(forms.ModelForm):
    class Meta:
        model = Truck_Type
        fields = ['truck_type', 'load_tonnage']


class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['product_name', 'product_description', 'UOM', 'truck_type']


class Fuel_Service_ProvidersForm(forms.ModelForm):
    class Meta:
        model = Fuel_Service_Providers
        fields = ['registered_name', 'trading_name', 'billing_address', 'supplier_TIN',
                  'supplier_VAT', 'email_address']


class Transporter_OrderForm(forms.ModelForm):
    class Meta:
        model = Transporter_Order
        fields = ['order_number', 'date', 'sales_order', 'transporter', 'driver', 'truck_reg_number',
                  'trailer1_reg_number', 'trailer2_reg_number', 'container_number', 'booking_ref', 'route',
                  'product', 'charge', 'charge_type', 'customer_invoice_number', 'POD_number']


class Transporter_PaymentForm(forms.ModelForm):
    class Meta:
        model = Transporter_Payment
        fields = ['date', 'transporter', 'payment_type', 'source_ref', 'truck_reg_number',
                  'service_provider', 'quantity', 'unit_price', 'payment_amount', 'matched_orders']


class Transporter_StatementForm(forms.ModelForm):
    class Meta:
        model = Transporter_Statement
        fields = ['transporter_name', 'date_from', 'date_to']

        # forms.py
        from django import forms
        from django.contrib.auth.models import User
        from .models import UserProfile

class UserRegistrationForm(forms.ModelForm):
            username = forms.CharField(max_length=150, required=True)
            password = forms.CharField(widget=forms.PasswordInput, required=True)
            email = forms.EmailField(required=True)
            first_name = forms.CharField(max_length=30, required=True)
            last_name = forms.CharField(max_length=30, required=True)
            phone_number = forms.CharField(max_length=15, required=False)

            class Meta:
                model = User
                fields = ['username', 'email', 'first_name', 'last_name', 'password']

            def save(self, commit=True):
                user = super().save(commit=False)
                user.set_password(self.cleaned_data['password'])  # Hash the password
                if commit:
                    user.save()
                    UserProfile.objects.create(user=user, phone_number=self.cleaned_data['phone_number'])
                return user

