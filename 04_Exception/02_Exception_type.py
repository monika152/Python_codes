x = 0 
# Versuchen : Risiko code
try:
    x = int (input("Enter 1 number: "))
    y = int (input("Enter 2 number:"))

    result = x / y

except ValueError as e:
    print("[Error: 1001]",e, "\n","Please enter a valid number between 0-9")

except ZeroDivisionError as e:
    print("[Error:1002]", e, "\n","You can not divide")

except Exception as e:
    print("[Error: 1003]",e, "\n" ,"This is an error") # TODO wann bekommt man diese error.

else:
    print(f"{x}/{y}= {result} ")

finally:
    print("Aufwidersehen")
print("Endee")