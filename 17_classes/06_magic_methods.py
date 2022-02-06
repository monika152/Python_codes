class Car:
    def __init__(self,model,kz,km,price)-> None:
        self.model = model
        self.kz = kz
        self.km = km
        self.price = price

    def show_data(self):
        print(f"model:{self.model} -kz:{self.kz}")

    def print_data(self):
        print(f"model:{self.model} -kz:{self.kz}")

    def __str__(self):
        return f"model:{self.model} -kz:{self.kz}"

    def __gt__(self,other):
        return self.price > other.price

    def __eq__(self,other):
        return self.price == other.price

    

# Creating an instance
tiguan = Car("Tiguan","AA123445",50000,15000)
touran = Car("Touran","AA123445",50000,15000)

print(tiguan)
print(touran)

tiguan.show_data()
touran.show_data()

print(tiguan.print_data())
print(touran.print_data())

print(tiguan)
print(touran)
print()
###############################

print(tiguan>touran)
print(tiguan==touran)


















# 


