from faker import Faker
import json, datetime, random, jsbeautifier
from Person import Person
from Operation import Operation
from Geography import City

def saveJson(entity,filename):
    with open(filename,'w') as jsonfile:
        
        # toWrite = jsbeautifier.beautify(json.dumps(e.get_item()))
        toWrite = json.dumps([e.get_item() for e in entity])
        jsonfile.write(toWrite)

def daterange(start_date, end_date):
    for n in range(int((end_date+datetime.timedelta(1) - start_date).days)):
        yield start_date + datetime.timedelta(n)

def vacations(date):
    if date.month in [6,7,8]:
        return 0.6
    else:
        return 1

def rebajasProb(date):
    if date.month in [1]:
        return 1
    else:
        return 0.8


def main():
    numPersonas = 20
    numCiudades = 5
    minDate = datetime.date(2020,1,1)
    maxDate = datetime.date(2020,12,31)
    Geo = [City(i) for i in range(1,numCiudades+1)]
    People = [Person(i,random.choice(Geo)) for i in range(1,numPersonas+1)]
    Operations = []
    for p in People:
        print('%s de %s' % (p.id,len(People)))
        for d in daterange(minDate, maxDate):
            if(rebajasProb(d)*vacations(d) * random.random() > (1 - p.actividad)):
                Operations.append(Operation(p,d,Geo))
    saveJson(People,'People.json')
    saveJson(Geo,'Geo.json')
    saveJson(Operations,'Operations.json')

main()