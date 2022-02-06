x =0
try:
        
    x = int(input("Enter a positive number:"))

    if x< 0:
            raise ValueError("Your Input is not a positive Number !!!") # manual Error

except ValueError as e:
    print(e) # Your input is not a positive number !!

else:
    print("X:", x)

print("Endee") 