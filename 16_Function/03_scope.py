location = "Berlin"

def greeting_1():
    print(location)

def greeting_2():
    location ="Hamburg" # creates a new local variable
    print(location) #Hamburg


def greeting_3():
    global location # makes the global variable editable
    location ="Aachen" # creates a new local variable
    print(location)#"Aachen"

def outer_function():
    x=10

    def inner_fuction():
        nonlocal x # makes the x from outer function editable
        x=20 # create a new local variable
        print("X(inner):",x) #20
            
    inner_fuction()
    print("X(outer):",x) #20


##############################
# calling
greeting_1()
greeting_2()

print(location)# Berlin

greeting_3()
print(location)# Aachen


outer_function()