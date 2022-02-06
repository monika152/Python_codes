# online shopping 
print("Wilkommen bei Online shopping")
age = int(input("enter your age"))
payment_method = True 

if age >= 18 and payment_method == True:
    print("sie können zur kasse gehen")
elif age >= 18 and payment_method == False:
    print("bitte bezahlung method eingeben")
elif age < 18 and payment_method ==True:
    print("Sie sind zu jung")
elif age >= 18 and payment_method == False: 
    print("sie brauchen bezahlung method")

    ##########################################