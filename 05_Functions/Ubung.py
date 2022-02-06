def FIZZBUZZ():

    user_input = int(input("Enter the number"))

    if user_input % 3 == 0 and user_input % 5 ==0:
        print("FIZZBUZZ")
    elif user_input % 5 == 0:
        print("FIZZ")
    elif user_input % 3 == 0:
        print("BUZZ")
    else:
        print(user_input)


FIZZBUZZ()

