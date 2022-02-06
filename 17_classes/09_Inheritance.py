class Car:
    def __init__(self,model,kz,km)->None:
        self.model = model 
        self.kz = kz
        self.km = km

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

class Audi(Car):
    def __init__(self,model,kz,km,panorama)->None:
        super().__init__(model,kz,km,)
        self.panorama=panorama

    def pnaorama_open(self):
        print("panorama is opening")


class Tesla(Car):
    def __init__(self,model,kz,km,battery)->None:
        super().__init__(model,kz,km,)
        self.battery=battery

    def battery_charge(self):
        print("Battery is charging")



# Creatte instance
VW_1 = VW("Passat","AA12345","5000",True)
audi_1 = Audi("Q4","BB12345","6000",True)
tesla_1 = Tesla("Passat","AA12345","5000",True)

list_car = [VW_1,audi_1,tesla_1]

for car in list_car:
    car.drive()
print()

for car in list_car:
    car.park()

for car in list_car:
    car.clean()