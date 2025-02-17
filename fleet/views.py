from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Sum
from datetime import datetime, timedelta
from django.shortcuts import redirect, get_object_or_404
from .forms import UserRegistrationForm
from .models import (Route, Products, Fuel_Service_Providers, Transporter_Order,
                     Transporter_Payment, Sales_Order, Customer_Registration,
                     Transporter_Registration, Transporter_Statement, Truck_Type)


# Home Page
def home(request):
    return render(request, 'fleet/home.html')


def dashboard_view(request):
    return render(request, 'fleet/dashboard.html')


def finance_clerk_dashboard(request):
    transporter_payment = Transporter_Payment.objects.filter(status='Pending')
    return render(request, 'fleet/finance_clerk_dashboard.html',{'transporter_payment': transporter_payment})


def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()
            messages.success(request, "Registration successful!")
            return redirect('login')  # Redirect to a login page or another page
    else:
        form = UserRegistrationForm()

    return render(request, 'signup.html', {'form': form})


# Route View
def route(request):
    if request.method == 'POST':
        try:
            # Create a new route in the database
            Route.objects.create(
                route_name=request.POST.get('route_name'),
                loading_point=request.POST.get('loading_point'),
                offloading_point=request.POST.get('offloading_point'),
                number_of_checkpoints=request.POST.get('number_of_checkpoints'),
                checkpoints=request.POST.get('checkpoints')
            )
            # Add a success message
            messages.success(request, "Route created successfully!")
        except Exception as e:
            # Add an error message if something goes wrong
            messages.error(request, f"Error creating route: {e}")
        # Redirect to the same page after form submission
        return redirect('route')  # Ensure this URL name matches your URL configuration

    # Render the form template with initial empty values
    return render(request, 'Route.html', {
        'route_name': '',
        'loading_point': '',
        'offloading_point': '',
        'number_of_checkpoints': '',
        'checkpoints': ''
    })


# Products View
def products(request):
    if request.method == 'POST':
        try:
            # Create a new product in the database
            Products.objects.create(
                product_name=request.POST.get('product_name'),
                product_description=request.POST.get('product_description'),
                UOM=request.POST.get('UOM'),
                truck_type=request.POST.get('truck_type')
            )
            # Add a success message
            messages.success(request, "Product created successfully!")
        except Exception as e:
            # Add an error message if something goes wrong
            messages.error(request, f"Error creating product: {e}")
        # Redirect to the same page after form submission
        return redirect('products')  # Ensure this URL name matches your URL configuration

    # Render the form template
    return render(request, 'Products.html', {})


# Customer Registration View
def customer_registration(request):
    if request.method == 'POST':
        try:
            # Create a new customer in the database
            Customer_Registration.objects.create(
                registered_name=request.POST.get('registered_name'),
                trading_name=request.POST.get('trading_name'),
                billing_address=request.POST.get('billing_address'),
                customer_TIN=request.POST.get('customer_TIN'),
                customer_VAT=request.POST.get('customer_VAT'),
                email_address=request.POST.get('email_address')
            )
            # Add a success message
            messages.success(request, "Customer registered successfully!")
        except Exception as e:
            # Add an error message if something goes wrong
            messages.error(request, f"Error registering customer: {e}")
        # Redirect to the same page after form submission
        return redirect('customer_registration')  # Ensure this URL name matches your URL configuration

    # Render the form template
    return render(request, 'Customer_Registration.html', {})


# Fuel Service Providers View
def fuel_service_providers(request):
    if request.method == 'POST':
        try:
            # Create a new fuel service provider in the database
            Fuel_Service_Providers.objects.create(
                registered_name=request.POST.get('registered_name'),
                trading_name=request.POST.get('trading_name'),
                billing_address=request.POST.get('billing_address'),
                supplier_TIN=request.POST.get('supplier_TIN'),
                supplier_VAT=request.POST.get('supplier_VAT'),
                email_address=request.POST.get('email_address')
            )
            # Add a success message
            messages.success(request, "Fuel service provider added successfully!")
        except Exception as e:
            # Add an error message if something goes wrong
            messages.error(request, f"Error adding provider: {e}")
        # Redirect to the same page after form submission
        return redirect('fuel_service_providers')  # Ensure this URL name matches your URL configuration

    # Render the form template
    return render(request, 'Fuel_Service_Providers.html', {})

# Sales Order View
def sales_order(request):
    if request.method == 'POST':
        try:
            # Retrieve the customer, product, and route based on the submitted names
            customer_name = request.POST.get('customer')
            product_name = request.POST.get('product')
            route_id = request.POST.get('route')  # Get the route ID from the POST data

            # Get the customer and product instances
            customer = Customer_Registration.objects.get(registered_name=customer_name)
            product = Products.objects.get(product_name=product_name)
            route = Route.objects.get(id=route_id)  # Retrieve the Route instance using the ID

            # Create a new sales order in the database
            Sales_Order.objects.create(
                date=request.POST.get('date'),
                customer=customer,  # Use the retrieved customer instance
                product=product,    # Use the retrieved product instance
                quantity=request.POST.get('quantity'),
                UOM=request.POST.get('UOM'),
                truck_type=request.POST.get('truck_type'),
                number_of_trucks=request.POST.get('number_of_trucks'),
                route=route,  # Use the retrieved Route instance
                number_of_trucks_remaining=request.POST.get('number_of_trucks_remaining'),
                number_of_trucks_allocated=0  # Set default value or retrieve from form if needed
            )
            # Add a success message
            messages.success(request, "Sales order created successfully!")
        except Customer_Registration.DoesNotExist:
            messages.error(request, "Customer not found.")
        except Products.DoesNotExist:
            messages.error(request, "Product not found.")
        except Route.DoesNotExist:
            messages.error(request, "Route not found.")
        except Exception as e:
            messages.error(request, f"Error creating sales order: {e}")
        # Redirect to the same page after form submission
        return redirect('sales_order')  # Ensure this URL name matches your URL configuration

    # Render the form template with initial empty values
    return render(request, 'Sales_Order.html', {
        'date': '',
        'customers': Customer_Registration.objects.all(),
        'products': Products.objects.all(),
        'quantity': '',
        'UOM': '',
        'truck_type': '',
        'number_of_trucks': '',
        'route': Route.objects.all()
    })
def transport_order(request):
    if request.method == 'POST':
        try:
            # Retrieve the selected IDs from the POST data
            transporter_id = request.POST.get('transporter')
            route_id = request.POST.get('route')
            product_id = request.POST.get('product')
            sales_order_id = request.POST.get('sales_order')

            # Print the received POST data for debugging
            print("Received POST data:")
            print(f"Transporter ID: {transporter_id}")
            print(f"Route ID: {route_id}")
            print(f"Product ID: {product_id}")
            print(f"Sales Order ID: {sales_order_id}")
            print(f"Order Number: {request.POST.get('order_number')}")
            print(f"Date: {request.POST.get('date')}")
            print(f"Driver: {request.POST.get('driver')}")
            print(f"Truck Reg Number: {request.POST.get('truck_reg_number')}")
            print(f"Trailer 1 Reg Number: {request.POST.get('trailer1_reg_number')}")
            print(f"Trailer 2 Reg Number: {request.POST.get('trailer2_reg_number')}")
            print(f"Container Number: {request.POST.get('container_number')}")
            print(f"Booking Ref: {request.POST.get('booking_ref')}")
            print(f"Charge: {request.POST.get('charge')}")
            print(f"Charge Type: {request.POST.get('charge_type')}")
            print(f"Customer Invoice Number: {request.POST.get('customer_invoice_number')}")
            print(f"POD Number: {request.POST.get('POD_number')}")
            print(f"Route: {route_id}")
            print(f"Product: {product_id}")

            # Validate that all required fields are present
            if not all([transporter_id, route_id, product_id, sales_order_id]):
                messages.error(request, "All fields are required.")
                return redirect('transport_order')

            # Fetch the related instances using get_object_or_404
            transporter = get_object_or_404(Transporter_Registration, id=transporter_id)
            route = get_object_or_404(Route, id=route_id)
            product = get_object_or_404(Products, id=product_id)
            sales_order = get_object_or_404(Sales_Order, id=sales_order_id)

            # Create the Transporter Order
            Transporter_Order.objects.create(
                order_number=request.POST.get('order_number'),
                date=request.POST.get('date'),
                sales_order=sales_order,
                transporter=transporter,
                driver=request.POST.get('driver'),
                truck_reg_number=request.POST.get('truck_reg_number'),
                trailer1_reg_number=request.POST.get('trailer1_reg_number'),
                trailer2_reg_number=request.POST.get('trailer2_reg_number'),
                container_number=request.POST.get('container_number'),
                booking_ref=request.POST.get('booking_ref'),
                charge=request.POST.get('charge'),
                charge_type=request.POST.get('charge_type'),
                customer_invoice_number=request.POST.get('customer_invoice_number'),
                POD_number=request.POST.get('POD_number'),
                route=route,
                product=product
            )

            messages.success(request, "Transport order created successfully!")
            return redirect('transport_order')  # Ensure this URL name matches your URL configuration
        except Exception as e:
            messages.error(request, f"Error creating transport order: {e}")
            print(f"Exception: {e}")  # Print the exception for debugging

    # Fetch all necessary data for the form
    transporters = Transporter_Registration.objects.all()
    routes = Route.objects.all()
    products = Products.objects.all()
    sales_orders = Sales_Order.objects.all()

    return render(request, 'Transport_Order.html', {
        'transporters': transporters,
        'routes': routes,
        'products': products,
        'sales_orders': sales_orders,
    })
# Transporter Statement View
def transporter_statement(request):
    if request.method == 'POST':
        try:
            Transporter_Statement.objects.create(
                transporter_name=request.POST.get('transporter_name'),
                date_from=request.POST.get('date_from'),
                date_to=request.POST.get('date_to')
            )
            messages.success(request, "Transport order created successfully!")
        except Exception as e:
            messages.error(request, f"Error creating transport order: {e}")
        return redirect('transporter_statement')  # Update with the correct URL name
    return render(request, 'Transporter_Statement.html', {})


# Transporter Registration View
def transporter_registration(request):
    if request.method == 'POST':
        try:
            # Create a new Transporter_Registration entry
            Transporter_Registration.objects.create(
                transporter_name=request.POST.get('transporter_name'),
                address=request.POST.get('address'),
            )
            # Success message
            messages.success(request, "Transporter registration created successfully!")
        except Exception as e:
            # Error message if something goes wrong
            messages.error(request, f"Error creating registration: {e}")
        # Redirect to the same page after submission
        return redirect('transporter_registration')  # Ensure this URL name is correct

    # Fetch all registered transporters for display in the table
    transporters = Transporter_Registration.objects.all().order_by('-id')

    # Render the form template for GET requests
    return render(request, 'Transporter_Registration.html', {
        'transporters': transporters,  # Pass the transporters data to the template
    })


# Transporter Payment View
def transporter_payment(request):
    if request.method == 'POST':
        try:
            Transporter_Payment.objects.create(
                date=request.POST.get('date'),
                transporter=request.POST.get('transporter'),
                payment_type=request.POST.get('payment_type'),
                source_ref=request.POST.get('source_ref'),
                truck_reg_number=request.POST.get('truck_reg_number'),
                service_provider=request.POST.get('service_provider'),
                quantity=request.POST.get('quantity'),
                unit_price=request.POST.get('unit_price'),
                payment_amount=request.POST.get('payment_amount'),
                matched_orders=request.POST.get('matched_orders')
            )
            messages.success(request, "Transport payment created successfully!")
        except Exception as e:
            messages.error(request, f"Error creating transport payment: {e}")
        return redirect('transporter_payment')  # Ensure this URL name is correct
    return render(request, 'Transporter_Payment.html', {})


# Truck Type View
def truck_type(request):
    if request.method == 'POST':
        try:
            # Create a new Truck_Type entry
            Truck_Type.objects.create(
                truck_type=request.POST.get('truck_type'),
                load_tonnage=request.POST.get('load_tonnage')
            )
            # Success message
            messages.success(request, "Truck type form created successfully!")
        except Exception as e:
            # Error message if something goes wrong
            messages.error(request, f"Error creating truck type: {e}")
        # Redirect to the same page after submission
        return redirect('truck_type')  # Ensure this URL name is correct
    # Render the form template for GET requests
    return render(request, 'Truck_Type.html', {})


def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to a login page or another page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'signup.html', {'form': form})


def operator_dashboard(request):
    current_month = datetime.now().month
    current_year = datetime.now().year

    # Total number of transporters
    total_transporters = Transporter_Registration.objects.all().count()

    # Fetch all transporters to display in the table
    transporters = Transporter_Registration.objects.all()

    # Count of transporters with status 'Approved'
    total_trucks_required_count = Sales_Order.objects.filter(status='Approved').count()

    # Sum of number_of_trucks for transporters with status 'Approved'
    total_trucks_required = \
        Sales_Order.objects.filter(status='Approved').aggregate(total_trucks=Sum('number_of_trucks_remaining'))[
            'total_trucks']

    # If no approved transporters, set total_trucks_approved to 0
    if total_trucks_required is None:
        total_trucks_required = 0

    # Fetch all sales orders to display in the table
    pending_orders = Sales_Order.objects.exclude(number_of_trucks_remaining=0)

    return render(request, 'fleet/operator_dashboard.html', {
        'total_transporters': total_transporters,
        'transporters': transporters,  # Pass the transporters data to the template
        'total_trucks_required_count': total_trucks_required_count,
        'total_trucks_required': total_trucks_required,
        'pending_orders': pending_orders,  # Pass the sales orders data to the template
    })


def sales_rep_dashboard(request):
    current_month = datetime.now().month
    current_year = datetime.now().year
    total_sales_orders = Sales_Order.objects.filter(date__month=current_month, date__year=current_year).count()
    total_customers = Customer_Registration.objects.all().count()
    pending_sales_orders = Sales_Order.objects.filter(status='Pending').count()
    approved_sales_orders = Sales_Order.objects.filter(status='Approved').count()
    pending_orders = Sales_Order.objects.filter(status='Pending')
    return render(request, 'fleet/sales_rep_dashboard.html',
                  {'total_sales_orders': total_sales_orders, 'total_customers': total_customers,
                   'pending_sales_orders': pending_sales_orders,
                   'approved_sales_orders': approved_sales_orders,
                   'pending_orders': pending_orders})


def sales_order_reports_view(request):
    # Query all records from the fleet_sales_order table
    orders = Sales_Order.objects.all().order_by('-id')
    # Pass the data to the template
    return render(request, 'sales_order_reports.html', {'orders': orders})


def products_summary_view(request):
    # Query all records from the fleet_sales_order table
    products = Products.objects.all().order_by('-id')
    # Pass the data to the template
    return render(request, 'products_summary.html', {'products': products})


def registered_customers_view(request):
    # Query all records from the fleet_sales_order table
    registered_customers = Customer_Registration.objects.all()
    # Pass the data to the template
    return render(request, 'registered_customer.html', {'registered_customers': registered_customers})


def registered_transporter_view(request):
    # Query all records from the fleet_sales_order table
    registered_transporter = Transporter_Registration.objects.all()
    # Pass the data to the template
    return render(request, 'registered_transporter.html', {'registered_transporter': registered_transporter})


def transport_order_summary_view(request):
    # Query all records from the fleet_sales_order table
    transport_order_raised = Transporter_Order.objects.all()
    # Pass the data to the template
    return render(request, 'transport_order_summary.html', {'transport_order_raised': transport_order_raised})


def registered_routes_view(request):
    # Query all records from the fleet_sales_order table
    registered_routes = Route.objects.all()
    # Pass the data to the template
    return render(request, 'registered_routes.html', {'registered_routes': registered_routes})


def registered_truck_types(request):
    # Query all records from the fleet_sales_order table
    registered_truck_types = Truck_Type.objects.all()
    # Pass the data to the template
    return render(request, 'registered_truck_types.html', {'registered_truck_types': registered_truck_types})


def operations_manager_dashboard(request):
    current_month = datetime.now().month
    current_year = datetime.now().year
    pending_sales_orders = Sales_Order.objects.filter(status='Pending').count()
    registered_customer = Customer_Registration.objects.filter(status='Pending').count()
    total_truck_types = Truck_Type.objects.filter(status='Pending').count()
    products = Products.objects.filter(status='Pending').count()
    transporters = Transporter_Registration.objects.filter(status='Pending').count()
    routes = Route.objects.filter(status='Pending').count()
    transport_order = Transporter_Order.objects.filter(status='Pending').count()
    return render(request, 'fleet/operations_manager_dashboard.html', {'pending_sales_orders': pending_sales_orders,
                                                                       'registered_customer': registered_customer,
                                                                       'total_truck_types': total_truck_types,
                                                                       'products': products,
                                                                       'transporters': transporters,
                                                                       'routes': routes,
                                                                       'transport_order': transport_order
                                                                       })

def finance_manager_dashboard(request):
    current_month = datetime.now().month
    current_year = datetime.now().year
    pending_sales_orders = Sales_Order.objects.filter(status='Pending').count()
    pending_payments = Transporter_Payment.objects.filter(status='Pending').count()
    registered_customer = Customer_Registration.objects.filter(status='Pending').count()
    total_truck_types = Truck_Type.objects.filter(status='Pending').count()
    products = Products.objects.filter(status='Pending').count()
    transporters = Transporter_Registration.objects.filter(status='Pending').count()
    routes = Route.objects.filter(status='Pending').count()
    transport_order = Transporter_Order.objects.filter(status='Pending').count()
    return render(request, 'fleet/finance_manager_dashboard.html', {'pending_sales_orders': pending_sales_orders,
                                                                       'registered_customer': registered_customer,
                                                                       'total_truck_types': total_truck_types,
                                                                       'products': products,
                                                                       'transporters': transporters,
                                                                       'routes': routes,
                                                                       'transport_order': transport_order,
                                                                    'pending_payments':pending_payments
                                                                       })


def director_dashboard(request):
    current_month = datetime.now().month
    current_year = datetime.now().year
    pending_sales_orders = Sales_Order.objects.filter(status='Pending').count()
    registered_customer = Customer_Registration.objects.filter(status='Pending').count()
    total_truck_types = Truck_Type.objects.filter(status='Pending').count()
    products = Products.objects.filter(status='Pending').count()
    transporters = Transporter_Registration.objects.filter(status='Pending').count()
    routes = Route.objects.filter(status='Pending').count()
    transport_order = Transporter_Order.objects.filter(status='Pending').count()
    return render(request, 'fleet/director_dashboard.html', {'pending_sales_orders': pending_sales_orders,
                                                             'registered_customer': registered_customer,
                                                             'total_truck_types': total_truck_types,
                                                             'products': products,
                                                             'transporters': transporters,
                                                             'routes': routes,
                                                             'transport_order': transport_order
                                                             })


def operations_manager_PSO_view(request):
    order = Sales_Order.objects.filter(status='Pending')
    return render(request, 'operations_manager_PSO.html', {'order': order, })
def payment_report(request):
    transporter_payment= Transporter_Payment.objects.all()
    return render(request, 'payment_report.html', {'transporter_payment': transporter_payment })


def operations_manager_PRC_view(request):
    registered_customer = Customer_Registration.objects.filter(status='Pending')
    return render(request, 'operations_manager_PRC.html', {'registered_customer': registered_customer})


def operations_manager_PTT_view(request):
    truck_type = Truck_Type.objects.filter(status='Pending')
    return render(request, 'operations_manager_PTT.html', {'truck_type': truck_type})

def payments_appending_approval(request):
    payments_pending = Transporter_Payment.objects.filter(status='Pending')
    return render(request, 'payments_appending_approval.html', {'payments_pending': payments_pending})


def operations_manager_Pending_Products_view(request):
    products = Products.objects.filter(status='Pending')
    return render(request, 'operations_manager_Pending_Products.html', {'products': products})


def operations_manager_Pending_Transporters(request):
    transporter = Transporter_Registration.objects.filter(status='Pending')
    return render(request, 'operations_manager_Pending_Transporters.html', {'transporter': transporter})


def operations_manager_Pending_Routes(request):
    route = Route.objects.filter(status='Pending')
    return render(request, 'operations_manager_Pending_Routes.html', {'route': route})


def operations_manager_Pending_Transport_Orders(request):
    transport_order = Transporter_Order.objects.filter(status='Pending')
    return render(request, 'operations_manager_Pending_Transport_Orders.html', {'transport_order': transport_order})

########################################################################################################################
# Operations Manager Approve and Decline Buttons for Sales Orders
def approve_order(request, order_id):
    order = get_object_or_404(Sales_Order, id=order_id)
    order.status = 'Approved'  # Set the status to Approved
    order.save()  # Save the changes to the database
    return redirect('operations_manager_PSO')  # Redirect to the appropriate page

def decline_order(request, order_id):
    order = get_object_or_404(Sales_Order, id=order_id)
    order.status = 'Declined'  # Set the status to Declined
    order.save()  # Save the changes to the database
    return redirect('operations_manager_PSO')  # Redirect to the appropriate page

########################################################################################################################
# Operations Manager Approve and Decline Buttons for Customers
def approve_customer(request, customer_id):
    customer = get_object_or_404(Customer_Registration, id=customer_id)
    customer.status = 'Approved'  # Set the status to Approved
    customer.save()  # Save the changes to the database
    return redirect('operations_manager_PRC')  # Redirect to the appropriate page

def decline_customer(request, customer_id):
    customer = get_object_or_404(Customer_Registration, id=customer_id)
    customer.status = 'Declined'  # Set the status to Declined
    customer.save()  # Save the changes to the database
    return redirect('operations_manager_PRC')  # Redirect to the appropriate page
########################################################################################################################
# Operations Manager Approve and Decline Buttons for Truck types
def approve_truck_type(request, truck_type_id):
    truck_type = get_object_or_404(Truck_Type, id=truck_type_id)
    truck_type.status = 'Approved'  # Set the status to Approved
    truck_type.save()  # Save the changes to the database
    return redirect('operations_manager_PTT')  # Redirect to the appropriate page

def decline_truck_type(request, truck_type_id):
    truck_type = get_object_or_404(Truck_Type, id=truck_type_id)
    truck_type.status = 'Declined'  # Set the status to Declined
    truck_type.save()  # Save the changes to the database
    return redirect('operations_manager_PTT')  # Redirect to the appropriate page
########################################################################################################################
# Operations Manager Approve and Decline Buttons for Products
def approve_product(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    product.status = 'Approved'  # Set the status to Approved
    product.save()  # Save the changes to the database
    return redirect('operations_manager_Pending_Products')  # Redirect to the appropriate page

def decline_product(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    product.status = 'Declined'  # Set the status to Declined
    product.save()  # Save the changes to the database
    return redirect('operations_manager_Pending_Products')  # Redirect to the appropriate page
########################################################################################################################
# Operations Manager Approve and Decline Buttons for Transporter
def approve_transporter(request, transporter_id):
    transporter = get_object_or_404(Transporter_Registration, id=transporter_id)
    transporter.status = 'Approved'  # Set the status to Approved
    transporter.save()  # Save the changes to the database
    return redirect('operations_manager_Pending_Transporters')  # Redirect to the appropriate page

def decline_transporter(request, transporter_id):
    transporter = get_object_or_404(Transporter_Registration, id=transporter_id)
    transporter.status = 'Declined'  # Set the status to Declined
    transporter.save()  # Save the changes to the database
    return redirect('operations_manager_Pending_Transporters')  # Redirect to the appropriate page
########################################################################################################################
# Operations Manager Approve and Decline Buttons for Routes
def approve_route(request, route_id):
    route = get_object_or_404(Route, id=route_id)
    route.status = 'Approved'  # Set the status to Approved
    route.save()  # Save the changes to the database
    return redirect('operations_manager_Pending_Routes')  # Redirect to the appropriate page

def decline_route(request, route_id):
    route = get_object_or_404(Route, id=route_id)
    route.status = 'Declined'  # Set the status to Declined
    route.save()  # Save the changes to the database
    return redirect('operations_manager_Pending_Routes')  # Redirect to the appropriate page
########################################################################################################################
# Operations Manager Approve and Decline Buttons for Transport Orders
def approve_transport_order(request, order_id):
    transport_order = get_object_or_404(Transporter_Order, id=order_id)
    transport_order.status = 'Approved'  # Set the status to Approved
    transport_order.save()  # Save the changes to the database
    return redirect('operations_manager_Pending_Transport_Orders')  # Redirect to the appropriate page

def decline_transport_order(request, order_id):
    transport_order = get_object_or_404(Transporter_Order, id=order_id)
    transport_order.status = 'Declined'  # Set the status to Declined
    transport_order.save()  # Save the changes to the database
    return redirect('operations_manager_Pending_Transport_Orders')  # Redirect to the appropriate page
########################################################################################################################
# Operations Manager Approve and Decline Buttons for Transporter Payment
def approve_transport_payment(request, payment_id):
    payment = get_object_or_404(Transporter_Payment, id=payment_id)
    payment.status = 'Approved'  # Set the status to Approved
    payment.save()  # Save the changes to the database
    return redirect('payments_appending_approval')  # Redirect to the appropriate page

def decline_transport_payment(request, payment_id):
    payment = get_object_or_404(Transporter_Payment, id=payment_id)
    payment.status = 'Declined'  # Set the status to Declined
    payment.save()  # Save the changes to the database
    return redirect('payments_appending_approval')  # Redirect to the appropriate page
########################################################################################################################
