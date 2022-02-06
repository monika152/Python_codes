for x in [1,2,3,4,5,6,7,8,9]:
    if x == 5:
        break
    print(x)


print("Ende")
print()
    ######################

for x in [1,2,3,4,5,6,7,8,9]:
    if x== 5:
        continue # jumbs the header of the loop for the the next iteration

    print(x)


user_input = ""

while True:

    user_input = int(input("Enter a positive number"))

    if user_input<0:
        print("This is a negative number , please enter only pos numbers")
        continue # jump to the header of the loop

    print(user_input)

    if user_input == 0:
        print("This is the exit point")
        break # exit loop

print("Ende")
