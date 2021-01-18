from faker import Faker
import json
import datetime
import random

class Person:
    def __init__(self):
        fake = Faker('es_ES')
        self.nombre = fake.first_name()
        self.apellido = fake.last_name()
        self.username = self.nombre[:3] + self.apellido[:3]
        self.email = fake.email()
        self.telefono = fake.phone_number()
        self.ciudad = fake.city()
        self.numcuenta = fake.bban()
        self.nacimiento = fake.date_of_birth(minimum_age=18,maximum_age=100)
        #self.historial = [Operation().get_item() for i in range(random.randint(0,10))]

    def get_item(self,i):
        p = {
            'id_persona': i,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'username': self.username,
            'email': self.email,
            'telefono': self.telefono,
            'ciudad': self.ciudad,
            'numcuenta': self.numcuenta,
            'nacimiento': self.nacimiento.strftime('%m/%d/%Y')#,
            #'historial de ventas': self.historial
        }
        return (p)
