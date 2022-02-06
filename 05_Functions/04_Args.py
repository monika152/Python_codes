# * tuple of all argumments

def addieren(*container):
    print("Container",container)
    for x in container: 
        print("X:",x)
    print()

    


addieren(2) #(2,)
addieren(5,9) # (5,9)
addieren(8,4,5,2,3,"A", True) # (8,4,5,2,3,'A',True)