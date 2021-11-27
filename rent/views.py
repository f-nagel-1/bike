from django.shortcuts import render
from .models import Rental
from datetime import date
from faker import Faker
from .models import *
import names

# Create your views here.

def rental(request):
    today = date.today()
    rentals = Rental.objects.filter(return_date__gte=today).order_by('return_date')
    #rental_list = []
    #print(today)
    # for value in rentals.all():
    #     rental_list.append(value.id)
    #     print(value.id)
    #     print(value.return_date)
    rentals_sorted = Rental.objects.filter().exclude(return_date__gte=today).order_by('return_date') 

    for value in rentals_sorted.all():
        #rental_list.append(value.id)
        print(value.id)
        print(value.return_date)

    return render(request, 'rental.html', {'rentals_sorted': rentals_sorted, 'rentals': rentals})


# def details(request):
#     rentals = rentals.objects.filter()
#     return render(request, 'rental.html', {'rentals_sorted': rentals_sorted, 'rentals': rentals})
# check how to send value in url (ID of rental)

def show_rental(request, rental_id):
    rental = Rental.objects.get(id=rental_id)
    print(rental)
    return render(request, 'show_rental.html', {'rental': rental})

def add_rental(request):
    if request.method == 'POST':
        customer = request.POST['customer']
        vehicle_type = request.POST['vehicle_type']
        print(customer, vehicle_type)
        try:
            cust_id = Customer.objects.get(id=customer)
            try:
                vehicle_type = Vehicle.objects.get(id=vehicle_type)
            except:
                vehicle_message = "Vehicle Type does not exist"
            return render(request, 'add.html', {'message': vehicle_message})
        #print(cust_id.id)
        except:
            message = "Customer ID does not exist"
            return render(request, 'add.html', {'message': message})
    return render(request, 'add.html')


def show_customer(request):
    customers = Customer.objects.all().order_by('first_name')
    print(customers)
    return render(request, 'customer.html', {'customers': customers})



def add_customer(request):
    if request.method == 'POST':
        customer = request.POST['customer']
        return render(request, 'add_customer.html', {'customer': customer})
   

# def add_customers(request):
#     # fake = Faker()
#     # print(fake.first_name())
#     for i in range(10):
#         print(names.get_full_name())
#     return render(request, 'rental.html')



        #name = 'Anna'
    #age = 20
    #subjects = ['apple', 'pears', 'oranges']
    #return render(request, 'rental.html', {'name': name, 'age': age, 'subjects': subjects})
    #today = date.today()