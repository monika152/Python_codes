class Employee: 
    
    # Class based attribute
    bonus = 500
   
   # Constructor
    def __init__(self,first_name,last_name,plz ="0000"):
        print("Instance is created",first_name,last_name)

        #   instance base attribute
        self.first_name = first_name
        self.last_name = last_name
        self.plz = plz
        self.city = ""
        self.car = ""
        


    # Method
    def greeting(self):
        print("Hallo,", self.first_name,self.last_name,self.plz)

# Creating instances-> Constructor Metthod (__init__) will be called automatically


emp_1 = Employee("Frank","Meier")# Frank
emp_2 = Employee("Sara","Meier","12345")
emp_3 = Employee("Lena","Meier","56789")
emp_4 = Employee("Lena","Meier","56789")

print("emp_1",emp_1.bonus) 
print("emp_2",emp_2.bonus) 
print("emp_3",emp_3.bonus) 
print("emp_4",emp_4.bonus)

# we don't find  bonus in the directory
print(emp_1.__dict__)
print(emp_2.__dict__)
print(emp_3.__dict__)
print(emp_4.__dict__)

print()
###########################################
emp_1.bonus = 700 # create a local value within the attribute
print("emp_1",emp_1.bonus)
print("emp_2",emp_2.bonus)
print("emp_3",emp_3.bonus)
print("emp_4",emp_4.bonus)

print(emp_1.__dict__)
print(emp_2.__dict__)
print(emp_3.__dict__)
print(emp_4.__dict__)

print()
######################################
# Change the class based attribute --> via class and not via the instance
Employee.bonus = 1000

print("emp_1",emp_1.bonus) # 700 --> local value from the instance
print("emp_2",emp_2.bonus) # 1000--> global class value
print("emp_3",emp_3.bonus) # 1000
print("emp_4",emp_4.bonus) # 1000

print(emp_1.__dict__)
print(emp_2.__dict__)
print(emp_3.__dict__)
print(emp_4.__dict__)