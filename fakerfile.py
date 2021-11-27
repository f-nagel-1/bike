# from django_seed import Seed

# seeder = Seed.seeder()

# from rent.models import Customer
# seeder.add_entity(Customer, 1)

# inserted_pks = seeder.execute()

# from faker import Faker
# from rent.models import Customer

# cus = Customer(faker.first_name(), last_name='Brown', email='test@gmail.com', address='Yellow road', city='Miami', country='Spain')
# cus.save()


from faker import Faker
import os
import django
import random

fake = Faker()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_store.settings')
django.setup()

from rent.models import *

def create_customer():
    for _ in range(20):
        Customer.objects.create(first_name = fake.first_name(), last_name = fake.last_name(), email = fake.email(), address = fake.address(), city = fake.city(), country = fake.country(),)


#create_customer()

