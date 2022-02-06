class Teilnehmer:  
   
   # Constructor
    def __init__(self,first_name,last_name,plz ="0000"):
        print("Instance is created",first_name,last_name)

        #   instance base attribute
        self.first_name = first_name
        self.last_name = last_name
        self.plz = plz
        self.salary = 0


    # Mehod
    def greeting(self):
        print("Hallo,", self.first_name,self.last_name,self.plz)

# Creating instances-> Constructor Metthod (__init__) will be called automatically
teilnehmer_1 = Teilnehmer("Frank","Meier")# Frank
teilnehmer_2 = Teilnehmer("Sara","Meier","12345")


# Show the attribute within the instance using __dict__
print(teilnehmer_1.__dict__)
print(teilnehmer_2.__dict__)

# show value of attributes
print(teilnehmer_1.first_name)
print(teilnehmer_1.last_name)

#change a value of attribute
teilnehmer_1.plz ="1111"
print(teilnehmer_1.plz)


print(teilnehmer_1.__dict__)
print(teilnehmer_2.__dict__)

# WARNING: In python you can create directly a new attribute via the instance
teilnehmer_1.banana ="300g"
print(teilnehmer_1.banana)

teilnehmer_2.car ="Audi"
print(teilnehmer_1.__dict__)
print(teilnehmer_2.__dict__)

# So teilnehmer_1 has "banana" and teilnehmer_2 haas "car"
print()
#############################################################
Teilnehmer_list = []
Teilnehmer_list.append(teilnehmer_1)
Teilnehmer_list.append(teilnehmer_2)

for teilnehmer in Teilnehmer_list:
    print(f"Teilnehmer: {teilnehmer.first_name} {teilnehmer.last_name}")