x = 0 
# Versuchen : Risiko code
try:
    x = int (input("Enter a number: ")) # 5
# Error
except Exception as e: # e:shows the error message from interperater
    print("This is an error")
    print(e)
# Kein Fehler
else:
    print(x) 

# Auf jedem fall finally wird ausgefürt
finally: 
    print("Aufwiedersehen !")

print() 
