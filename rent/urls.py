from django.urls import path
from . import views

urlpatterns = [
    path('rental', views.rental, name = 'rental'),
    path('rental/<int:rental_id>', views.show_rental, name = 'show_rental'),
    #path('add_customers', views.add_customers, name = 'add_customers'),
    path('rental/add', views.add_rental, name = 'add_rental'),
    path('customer', views.show_customer, name = 'show_customer'),
    path('customer/add_customer', views.add_customer, name = 'add_customer'),
]