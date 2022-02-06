# online shopping

age = 23
payment_method = True
if (age >= 18) and (payment_method == True):
    print("Sie dürfen zur kasse!")
elif (age < 18) and (payment_method == True):
    print("Sie sind zu jung")
elif (age >= 18) and (payment_method == False):
    print("Sie mussen Bezahlungsmethode eingeben")
elif (age < 18) and (payment_method == False):
    print("Sie sind zu jung und Sie müssen Bezahlung method eingeben")



##############################################
#online shopping

age = 15
payment_method = False #ich will das als user input haben also in terminal geben ung nicht ganz oben
items = 4

if age >= 18: #Adult
    if payment_method ==True:
        if items > 0:
            print("Sie dürfen zur kasse !")
        else:
            print("Sie benötigen Produkte bevor kasse!")
    else:
        print("Sie müssen BZ method eingeben")
else:
    print("sie sind zu jung!")


    ################################################

#online shopping
#einfachste Method

age = 17
payment_method = False
items = 0
customer_card =True 

message = ""

if(age >= 18) and (payment_method == True) and (items > 0) and (customer_card == True):
    message = "Sie dürfen zur kasse!"
else:
    if age < 18:
        message += "Sie sind  zu jung!\n"
    if payment_method == False:
        message += "Sie müssen BZ-method benötigen!\n"
    if items < 1:
        message += "Sie müssen produkte kaufen bevor kasse!\n"
    if customer_card == False:
        message += "Sie brauchen eine kundenkarte!\n"

print(message)







