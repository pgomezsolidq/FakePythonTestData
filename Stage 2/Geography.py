from faker import Faker
import random

class City:
    def __init__(self,i):
        fake = Faker('es_ES')
        self.id = i
        self.name = fake.city()
        self.stores = [Store(i) for i in range(1,random.randint(2,8))]
    def get_item(self):
        p = {
            'id_ciudad': self.id,
            'Ciudad': self.name,
            'Stores': [s.get_item() for s in self.stores]
        }
        return (p)

class Store:
    def __init__(self,i):
        fake = Faker('es_ES')
        self.id = i
        self.storeName = fake.company()
    def get_item(self):
        p = {
            'id_store': self.id,
            'Store': self.storeName
        }
        return (p)
    