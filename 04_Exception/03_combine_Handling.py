x = 0 
# Versuchen : Risiko code
try:
    x = int (input("Enter 1 number: "))
    y = int (input("Enter 2 number:"))

    result = x / y

except (ValueError , ZeroDivisionError) as e:
    print("[Error: 1001]",e, "\n","This is an Eror")

else:
    print(f"{x}/{y} = {result}")
finally:
    print("Aufwidersehen")

print("Endee")