from faker import Faker
import random

class Person:
    def __init__(self,i,city):
        fake = Faker('es_ES')
        self.id = i
        self.nombre = fake.first_name()
        self.apellido = fake.last_name()
        self.username = self.nombre[:3] + self.apellido[:3]
        self.email = fake.email()
        self.telefono = fake.phone_number()
        self.numcuenta = fake.bban()
        self.nacimiento = fake.date_of_birth(minimum_age=18,maximum_age=100)
        self.actividad = random.random()
        self.city = city
        self.mobility = (random.random()*random.random()*random.random())
    def get_item(self):
        p = {
            'id_persona': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'username': self.username,
            'email': self.email,
            'telefono': self.telefono,
            'numcuenta': self.numcuenta,
            'nacimiento': self.nacimiento.strftime('%m/%d/%Y'),
            'ciudad': self.city.name,
            'id_ciudad': self.city.id,
            'Movilidad': self.mobility
        }
        return (p)