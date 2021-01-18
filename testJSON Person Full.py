from faker import Faker
import json
import datetime
import random
#
class Operation:
    def __init__(self):
        fake = Faker('es_ES')
        self.valor = round(random.random()*random.random()*10000)
        self.tienda = fake.company()
    def get_item(self):
        p = {
            'valor': self.valor,
            'tienda': self.tienda 
        }
        return (p)
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
        self.historial = [Operation().get_item() for i in range(random.randint(0,10))]

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
            'nacimiento': self.nacimiento.strftime('%m/%d/%Y'),
            'historial de ventas': self.historial
        }
        return (p)

def generatePerson(num):
    People = [Person().get_item(i) for i in range(num)]
    filename = 'people.json'
    with open(filename,'w') as jsonfile:
        jsonfile.write(json.dumps(People))

def main():
    numPersonas = 20
    generatePerson(numPersonas)

main()