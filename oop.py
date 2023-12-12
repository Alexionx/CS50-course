'''
# Class приклад створення класу
class Point:
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2
        
p = Point(2, 8)
print(p.x)
print(p.y)
'''
'''
#Програма для відстеження бронювання квитків на рейс і щоб не було переповнення
class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
        
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
        
    def open_seats(self):
        return self.capacity - len(self.passengers)
        
Flight = Flight(3)

people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    if Flight.add_passenger(person):
        print(f"Added {person} to flight succesfully")
    else:
        print(f"No available seats for {person}")
'''

'''
#Декоратори в Python
def annuance(f):
    def wrapper():
        print ("About to run the function...")
        f()
        print("Done with the function")
    return wrapper

@annuance
def hello():
    print("Hello World")
    
hello()
'''

'''
#функція lmbda
people = [
    {"name": "Harry", "house": "Griffindor"},
    {"name": "Cho", "house": "Ravenclavr"},
    {"name": "Draco", "house": "Slytherin"}
]

people.sort(key=lambda person: person["name"])

print(people)
'''

'''
#Просте ділення в пайтон з бібліотекою sys для виходу з програми 
import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Erro: Invalid input")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1)
    

print(f"{x} / {y} = {result}")
'''
