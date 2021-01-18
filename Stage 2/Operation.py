from faker import Faker
import json
import datetime
import random

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
