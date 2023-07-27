from data.data import Person, Person_WebTabel
from faker import Faker
import random

faker_ru = Faker('ru_RU')
faker_en = Faker()

def generator_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
    )

def webtable_generator_person():
    yield Person_WebTabel(
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        email=faker_en.email(),
        age=random.randint(0, 99),
        salary=random.randint(0, 1000000),
        department=random.choice(['Compliance', 'Insurance', 'Legal', 'Sales'])
    )