# exit inf-loop --> ctrl+c = cancel

temprature = 35


while temprature > 30 :
    print("Klima an:", temprature)
    temprature -= 1

print("Ende")
print()
##################

command = ""

while command != "exit":
    command = input ("Enter a text:")
    print("Echo:", command)
print("Ende 2")

print()

#################
# print all no. from 1 to 10

number = 1

while number < 11:
    print(number)
    number+= 1
    print(" Ende 3")
   
    