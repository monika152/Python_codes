location = "Berlin"

# Read global variable from local scope
def greeting(first_name, last_name):
    print(location) # Read only global variable
    print("Hello", first_name, last_name)

greeting("Thomas","Meier")
location = "Hamburg"
greeting("Ingo","Meier")
    ########################################

def greeting2(first_name, last_name):
    location = "Aachen" # creates a new local variable
    print(location) 
    print("Hello", first_name, last_name)

greeting2("Sara","Meier")
print(location) # Hamburg

#####################################


def greeting3(first_name, last_name):
    global location # makes the global variable ->
    location = "Frankfurt"
    print(location)
    print("Hallo",first_name,last_name)

greeting3("Lena","Meier")
print(location) #Frankfurt

