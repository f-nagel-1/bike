from django.shortcuts import render
from .models import Rental
from datetime import date

# Create your views here.

def rental(request):

    rentals = Rental.objects.filter(customer_id=1)
    rental_list = []
    for value in rentals.all():
        rental_list.append(value.id)
        print(value.id)
    return render(request, 'rental.html')





        #name = 'Elena'
    #age = 20
    #subjects = ['apple', 'pears', 'oranges']
    #return render(request, 'rental.html', {'name': name, 'age': age, 'subjects': subjects})
    #today = date.today()