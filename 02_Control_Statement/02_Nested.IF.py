temperature = 25
klima_status ="an" #"aus"

if temperature >=30:
    if klima_status =="aus":
        print("klima an machen")
        klima_status = "an"
    else:
        print("klima ist sowieso an")
else: 
    if klima_status =="an":
        print("klima aus machen")
        klima_status = "aus"
        
    else:
        print("klima ist sowieso aus")
    
    

    ##########################################

