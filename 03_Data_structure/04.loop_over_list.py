teilnehmerliste = ["Thomas" ,"Ingo", "Sara","Lena","Jana","Matthias"]

counter = 1
for teilnehmer in teilnehmerliste:
    print(f"{counter}.",teilnehmer)
    counter += 1
print("\n\n")
#############################
user_data = ["Mattias", "Möller" ,55, 37.2 ,True ,["Jana ","Sara"]]

for x in user_data:
    print(x,type(x))


print("\n\n")
##########################
# enumerate() --< return a tuple (index, value)

teilnehmer = ["Thomas","Ingo","Sara", "Lena","Jana", "Matthias"]

for teilnehmer in enumerate(teilnehmerliste): #Tuple (0, "Thomas")
    print(teilnehmer) #(0,Thomas),(1,"ingo")
    print(f"Index:{teilnehmer[0]}-Value: {teilnehmer[1]}") #TODO: why f"Index:{teilnehmer[0]}
    print()

    # enumerate combined with unpacking
    for idx, val in enumerate(teilnehmerliste): #tuple (0,"Thomas")
        print(f"Index:{idx}-value: {val}")
        