import os
import random

from data.data import Person
from faker import Faker

fake_en = Faker('En')
Faker.seed()


def generated_person():
    yield Person(
        full_name=fake_en.first_name() + " " + fake_en.last_name(),
        firstname=fake_en.first_name(),
        lastname=fake_en.last_name(),
        age=random.randint(10, 80),
        salary=random.randint(10000, 100000),
        department=fake_en.job(),
        email=fake_en.email(),
        current_address=fake_en.address(),
        permanent_address=fake_en.address(),
        mobile=fake_en.msisdn(),
    )


def generate_file():
    current_directory = os.getcwd()
    path = os.path.join(current_directory, f'{random.randint(0,999)}.txt')
    file = open(path, 'w')
    file.write(f'Hello World{random.randint(0, 999)}')
    file.close()
    return file.name, path