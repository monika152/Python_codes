""""
Native Python dies not have abstrsct class,
therefore we use the built_in module ABC

abstract class: a class which can not be initiated
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Requirment:
~~~~~~~~~~~~~
1.
Benifits: 
~~~~~~~~~~~~
1. disable initi. an abstract class
2. Make sure that every child class has an implementation of abstract methods
"""
from abc import ABC, abstractmethod
# class car is abstract

class Car(ABC):
    def __init__(self,model,kz,km)->None:
        self.model = model 
        self.kz = kz
        self.km = km
    @abstractmethod
    def test(self):
        pass
    @abstractmethod
    def anmelden(self):
        pass
        raise NotImplementedError("Please implent in the child class")
    def drive(self):
        print("Car is driving perfectly..........")

    def park(self):
        print(" Car is parking.....!!!!")

    def clean(self):
        print("Car is cleaned.....!!")


class VW(Car):

    def __init__(self,model,kz,km,gps)->None:
        super().__init__(model,kz,km,)
        self.gps =gps 

    def gps_navi(self):
        print("GPS is navigating")

    def test(self):
        print("This is vw test")

    def anmelden(self):
        print("this is VW Anmeldung")

class Audi(Car):
    def __init__(self,model,kz,km,panorama)->None:
        super().__init__(model,kz,km,)
        self.panorama=panorama

    def pnaorama_open(self):
        print("panorama is opening")

    
    def test(self):
        print("This is Audi test")

    def anmelden(self):
        print("this is Audi  Anmeldung")


class Tesla(Car):
    def __init__(self,model,kz,km,battery)->None:
        super().__init__(model,kz,km,)
        self.battery=battery

    def battery_charge(self):
        print("Battery is charging")

        
    def test(self):
        print("This is Tesla test")

    def anmelden(self):
        print("this is Tesla Anmeldung")



# Creatte instance
VW_1 = VW("Passat","AA12345","5000",True)
audi_1 = Audi("Q4","BB12345","6000",True)
tesla_1 = Tesla("Passat","AA12345","5000",True)


VW_1.drive() 

VW_1.anmelden() 
audi_1.anmelden() 
tesla_1.anmelden() 
