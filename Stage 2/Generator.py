from faker import Faker
import json
import datetime
import random
from Person import Person
from Operation import Operation


def generatePerson(num):
    People = [Person().get_item(i) for i in range(num)]
    filename = 'people.json'
    with open(filename,'w') as jsonfile:
        jsonfile.write(json.dumps(People))

def main():
    numPersonas = 2
    generatePerson(numPersonas)

main()