from faker import Faker
import random

def rebajas(date):
    if date.month == 1:
        return  0.6
    else:
        return  1

class Operation:
    def __init__(self,person,date,geo):
        fake = Faker('es_ES')
        self.client = person
        self.city = None
        if (random.random() > person.mobility):
            self.city = person.city
        else:
            self.city = random.choice(geo)
        self.store = random.choice(self.city.stores)
        self.date = date
        self.valor = round(rebajas(date)*random.random()*random.random()*10000)
        assert self.city != None
    def get_item(self):
        p = {
            'Valor': self.valor,
            'Cliente': self.client.id ,
            'Ciudad': self.city.id,
            'Tienda': self.store.id,
            'Fecha': self.date.strftime('%d/%m/%Y')
        }
        return (p)

