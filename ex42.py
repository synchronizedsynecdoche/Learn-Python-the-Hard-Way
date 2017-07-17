##Animal is-an object
class Animal(object):
    pass

##Dog is-an animal is-an object
class Dog(Animal):
    def __init__(self,name):
        ##dog has-a name
        self.name=name
   
##Cat is-an animal is-an object
class Cat(Animal):
    def __init__(self,name):
        ##Cat has-a name
        self.name=name

#person is-an object
class Person(object):

    def __init__(self,name):
        ##Person has-a name
        self.name=name
        ##person has-a pet of some kind
        self.pet=None

##Employee is-a Person is-an object
class Employee(Person):
    def __init__(self,name,salary):
        ##hmm, what is this strange magic?
        super(Employee, self).__init__(name)
        ##Employee has-a salary
        self.salary=salary

##Fish is-an object
class Fish(object):
    pass

##Salmon is-a Fish is-an object
class Salmon(Fish):
    pass
##Halibut is-a Fish is-an object
class Halibut(Fish):
    pass

##rover is-a Dog
rover= Dog("Rover")

##satan is-a cat
satan=Cat("Satan")

##mary is-a person
mary=Person("Mary")

##marry has-a pet
mary.pet=satan

## frank is-an employee who has-a salary
frank=Employee("Frank", 120000)

##frank has-a pet named rover
frank.pet=rover

##flipper is-a fish
flipper=Fish()

##crouse is-a Salmon
crouse=Salmon()

##harry is-a Halibut
harry=Halibut()
