# import all function(s) and variables(s) locally
from wbsweiterbildung import *


weiterbildung_anmeldung()

print(first_name) # Thomas -value from the module but local variable



# Change the value of the variable which came from module but locally
first_name = "Sara"

print(first_name) # Sara
print(last_name) #Meier