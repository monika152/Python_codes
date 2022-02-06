for x in ["Thomas","Ingo","Frank","Sara"]:

    if x== "Frank":
        break # exits the loop completely
    else:
        print(x)

print("End of for loop")


###################################


for x in ["Thomas", "Ingo","Frank","Sara"]:

    if x== "Frank":
        break # exits the loop completely

    print(x)

    print("End of loop 2")

    print()


    #####################################
    for x in range(100): #[0->99]
        if x == 5:
            break
        print(x)

        ############################

temprature = 27
status = True
while status == True:
    print("temprature:", temprature)

    if temprature == 27:
        print("Hallo 27")
        break

    if temprature == 20:
        print("Hallo 20")
        break


    if temprature == 15:
        print("Hallo 15")
        break

    if temprature == 7:
        status = False

        temprature -=1

print("End of code 1")