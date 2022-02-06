x = 5
y = "Python"
z = 5.5

print(type(x))
print(type(y))
print(type(z))
print()
######################################
# Template-->class


class Teilnehmer:
  
    # Methods
    def greeting(self, name):
        print("Hallo,", name)


# Create the instance (copy*)


teilnehmer_1 = Teilnehmer()  # Mohamed


teilnehmer_2 = Teilnehmer()  # Thomas


# Run the Methods


teilnehmer_1.greeting("Mohamed")
teilnehmer_1.greeting("Thomas")

# Check Data Type


print(type(teilnehmer_1))
print(type(teilnehmer_2))

# compare Instance with class


print(isinstance(teilnehmer_1, Teilnehmer))  # True
print(isinstance(x, Teilnehmer))  # False