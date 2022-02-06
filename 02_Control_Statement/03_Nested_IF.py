

temprature = 0
user_input = int(input("Enter the temprature"))

print(user_input)

if temprature >= 30:
    print(" Es ist heiß")
elif  20 <= temprature > 30 :
    print("es ist warm")
elif 10 <= temprature < 20 :
    print("Es ist cool")
elif 0 < temprature < 10 :
    print("es ist kalt")
else:
    print("Es ist zu kalt")

# TODO: not working properly