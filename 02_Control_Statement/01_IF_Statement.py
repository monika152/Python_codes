temperature = 35

if temperature > 30:
    print("Es ist warm")
    print("Bitte klima an machen")
else:
        print("Es ist cool")
print("\n\n")
######################################

temperature = -5

if temperature >= 30:
    print("Es ist heiß")
elif temperature <30 and temperature >=20:
    print("Es ist warm")
elif temperature<20 and temperature>=10:
    print("Es ist cool")
elif temperature <10 and temperature >=0:
    print("Es ist kalt")
elif temperature <0:
    print("Es ist zu kalt")

print("\n\n")

###############
temperature = -5

if temperature >=30:
    print("Es ist heiß")
elif 20 <= temperature < 30 :
    print("Es ist warm")
elif 10 <= temperature <20 :
    print("Es ist cool")
elif 0<= temperature < 10 :
    print("Es ist kalt") 
else:
        print("Es ist zu kalt")
