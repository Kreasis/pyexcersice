#añades  valores a la lista y estos valores los das con el range
my_list = []
for val in range(0,11,1):
    my_list.append(val)
    print(my_list)

#
groceries = ['roast beef', 'cucumbers', 'lettuce', 'peanut butter', 'bread', 'dog food']
#sirve para enumerar una lista


for index, items in enumerate(groceries, 1):
    print (f'{index}. {items}')

    #dictioraries, como printear la key y el value

course = {'teacher':'Ashley', 'title':'Introducing Dictionaries', 'level':'Beginner'}

for key, value in course.items():
    print(key, value)
    
    #packing dictionaries
    #kwargs will pack variable arguments into a dictionary, 
    # not a tuple! Packing positional arguments into a tuple is denoted by *args.
def print_teacher(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')
    
print_teacher(name ='Ashley', job='Instructor', topic= 'Python')


#class propiedades
class Car:
    wheels =4
    doors = 2
    engine = True
    
    def __init__(self, model, year, make ="Ford"):
        self.make = make
        self.model = model
        self.year = year
        self.is_moving = False
        self.gas = 100
    def stop(self):
        if self.is_moving:
            print("the car stopped")
            self.is_moving = False
        else:
            print("the car has already stopped")
        
    def go(self, speed):
        if self.use_gas():
            if not self.is_moving:
                print("the car is moving")
                self.is_moving = True
            print(f'the car is going {speed}')
        else:
            print("you have run out of gas")
            self.stop()
    def use_gas(self):
        self.gas -= 50
        if self.gas <= 0:
            return False
        else:
            return True
        
car_one = Car("Model T", 1980)
car_one.stop()
car_one.go("20KM")              
car_one.go("120KM")               
car_two = Car("Tundra", 2021, "Toyota")
        
print(car_one.make)       
print(car_two.make)  
car_one.year = 2022
print(car_one.year)       
print(car_two.year)  

#dunder str iter
class Car:
    # Class Attributes
    wheels = 4
    doors = 2
    engine = True

    # The Initializer
    def __init__(self, model, year, make='Ford', gas=100):
        # Instance Attributes
        self.make = make
        self.model = model
        self.year = year
        self.gas = gas
        # instance attributes don't have
        # to be passed in
        self.is_moving = False
    def __str__(self):
        return f"{self.make} {self.model} {self.year}"

    def use_gas(self):
        self.gas -= 50
        if self.gas <= 0:
            return False
        return True

    def stop(self):
        if self.is_moving:
            print('The car has stopped.')
            self.is_moving = False
        else:
            print('The car has already stopped.')

    def go(self, speed):
        if self.use_gas():
            if not self.is_moving:
                print('The car starts moving.')
                self.is_moving = True
            print(f'The car is going {speed}.')
        else:
            print("You've run out of gas!")
            self.stop()

class Dealership:
    def __init__(self):
        self.cars =[]
    def __iter__(self):
        yield from  self.cars
    def add_car(self, car):
        self.cars.append(car)

car_one = Car('Toyota', 'Camry', 2020)
car_two = Car('Toyota', 'Fiesta', 2021)
car_tree = Car('Toyota', 'Hilux', 2022)
my_dealership = Dealership()
my_dealership.add_car(car_one) 
my_dealership.add_car(car_two)
my_dealership.add_car(car_tree)
for car in my_dealership:
    print(car)

# dunder eq
class Car:
    # Class Attributes
    wheels = 4
    doors = 2
    engine = True

    # The Initializer
    def __init__(self, model, year, make='Ford', gas=100):
        # Instance Attributes
        self.make = make
        self.model = model
        self.year = year
        self.gas = gas
        # instance attributes don't have
        # to be passed in
        self.is_moving = False
    def __str__(self):
        return f"{self.make} {self.model} {self.year}"
    def __eq__(self, other):
        return self.make == other.make and self.model == other.model
    def use_gas(self):
        self.gas -= 50
        if self.gas <= 0:
            return False
        return True

    def stop(self):
        if self.is_moving:
            print('The car has stopped.')
            self.is_moving = False
        else:
            print('The car has already stopped.')

    def go(self, speed):
        if self.use_gas():
            if not self.is_moving:
                print('The car starts moving.')
                self.is_moving = True
            print(f'The car is going {speed}.')
        else:
            print("You've run out of gas!")
            self.stop()

class Dealership:
    def __init__(self):
        self.cars =[]
    def __iter__(self):
        yield from  self.cars
    def add_car(self, car):
        self.cars.append(car)

car_one = Car('Toyota', 'Camry', 2020)
car_two = Car('Toyota', 'Fiesta', 2021)
car_tree = Car('Toyota', 'Hilux', 2022)
my_dealership = Dealership()
my_dealership.add_car(car_one) 
my_dealership.add_car(car_two)
my_dealership.add_car(car_tree)
for car in my_dealership:
    print(car)
    
    
if car_one == car_two:
    print("equal")
else:
    print("not equal")