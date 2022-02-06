
def greeting(first_name, last_name): # 2x Must parameter
    print(f"Hallo {first_name}, {last_name}")
    print("Wie geht es dir ?")
    print()

greeting("Monika","Singh")
greeting("Bhoopender", "Singh")
greeting("Rupesh" , "singh")


# Actung:
greeting(1,2) # Data Types
greeting("Singh", "Monika")
print("\n" * 5)
##########################################
# Default value
def greeting2(first_name, last_name="***"): # 1x Must Parameter,1x Param with default value
    print(f"Hallo {first_name}, {last_name}")
    print("Wie geht es dir ?")
    print()

    # Caller
greeting2("Ingo")
greeting2("Ingo", "Möller")


def area(x, y= "banana"):
    if y == "banana": #y: kommt von default
        y=x
    result = x* y
    print(f"Area{x}*{y}={result}")


area(3,5)
area(30,5)
area(7)
area(6,9)
area(4,)