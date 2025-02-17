from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views  # Import auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('sales_rep_dashboard/', views.sales_rep_dashboard, name='sales_rep_dashboard'),
    path('director_dashboard/', views.director_dashboard, name='director_dashboard'),
    path('registered_truck_types/', views.registered_truck_types, name='registered_truck_types'),
    path('operations_manager_dashboard/', views.operations_manager_dashboard, name='operations_manager_dashboard'),
    path('finance_manager_dashboard/', views.finance_manager_dashboard, name='finance_manager_dashboard'),
    path('operator_dashboard/', views.operator_dashboard, name='operator_dashboard'),
    path('finance_clerk_dashboard/', views.finance_clerk_dashboard, name='finance_clerk_dashboard'),
    path('payments_appending_approval/', views.payments_appending_approval, name='payments_appending_approval'),
    path('signup/', views.signup, name='signup'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('customer_registration/', views.customer_registration, name='customer_registration'),
    path('products/', views.products, name='products'),
    path('fuel_service_providers/', views.fuel_service_providers, name='fuel_service_providers'),
    path('route/', views.route, name='route'),
    path('sales_order/', views.sales_order, name='sales_order'),
    path('transport_order/', views.transport_order, name='transport_order'),
    path('transporter_payment/', views.transporter_payment, name='transporter_payment'),
    path('transporter_registration/', views.transporter_registration, name='transporter_registration'),
    path('transporter_statement/', views.transporter_statement, name='transporter_statement'),
    path('truck_type/', views.truck_type, name='truck_type'),
    path('sales_order_reports/', views.sales_order_reports_view, name='sales_order_reports'),
    path('products_summary/', views.products_summary_view, name='products_summary'),
    path('registered_customers/', views.registered_customers_view, name='registered_customers'),
    path('registered_transporter/', views.registered_transporter_view, name='registered_transporter'),
    path('transport_order_summary/', views.transport_order_summary_view, name='transport_order_summary'),
    path('registered_routes/', views.registered_routes_view, name='registered_routes'),
    path('payment_report/', views.payment_report, name='payment_report'),
    path('operations_manager_PSO/', views.operations_manager_PSO_view, name='operations_manager_PSO'),
    path('operations_manager_PRC/', views.operations_manager_PRC_view, name='operations_manager_PRC'),
    path('operations_manager_PTT/', views.operations_manager_PTT_view, name='operations_manager_PTT'),
    path('operations_manager_Pending_Transport_Orders/', views.operations_manager_Pending_Transport_Orders, name='operations_manager_Pending_Transport_Orders'),
    path('operations_manager_Pending_Routes/', views.operations_manager_Pending_Routes, name='operations_manager_Pending_Routes'),
    path('operations_manager_Pending_Transporters/', views.operations_manager_Pending_Transporters, name='operations_manager_Pending_Transporters'),
    path('operations_manager_Pending_Products/', views.operations_manager_Pending_Products_view, name='operations_manager_Pending_Products'),

    path('approve/<int:order_id>/', views.approve_order, name='approve_order'),  # operation manager approve button for sales orders
    path('decline/<int:order_id>/', views.decline_order, name='decline_order'),  # operation manager decline button for sales orders

    path('approve_customer/<int:customer_id>/', views.approve_customer, name='approve_customer'),
    path('decline_customer/<int:customer_id>/', views.decline_customer, name='decline_customer'),  # operation manager decline button for customers

    path('approve_truck_type/<int:truck_type_id>/', views.approve_truck_type, name='approve_truck_type'),
    path('decline_truck_type/<int:truck_type_id>/', views.decline_truck_type, name='decline_truck_type'), # operation manager decline button for truck types

    path('approve_product/<int:product_id>/', views.approve_product, name='approve_product'),
    path('decline_product/<int:product_id>/', views.decline_product, name='decline_product'),# buttons for products approval

    path('approve_transporter/<int:transporter_id>/', views.approve_transporter, name='approve_transporter'),
    path('decline_transporter/<int:transporter_id>/', views.decline_transporter, name='decline_transporter'), #buttons for transporter approval

    path('approve_route/<int:route_id>/', views.approve_route, name='approve_route'),
    path('decline_route/<int:route_id>/', views.decline_route, name='decline_route'),#buttons for approval for routes

    path('approve_transport_order/<int:order_id>/', views.approve_transport_order, name='approve_transport_order'),
    path('decline_transport_order/<int:order_id>/', views.decline_transport_order, name='decline_transport_order'),# transporter order approvals

    path('approve_payment/<int:payment_id>/', views.approve_transport_payment, name='approve_transport_payment'),
    path('decline_payment/<int:payment_id>/', views.decline_transport_payment, name='decline_transport_payment'), #payment approvals
]

admin.site.site_header = "Trucker Administration"
admin.site.site_title = "Trucks admin site"
admin.site.index_title = "Welcome to The Truck Company"