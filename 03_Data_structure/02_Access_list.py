teilnehmerliste = ["Thomas" , "Ingo" ,"Sara", "Monika"]


print(teilnehmerliste[0])
print(teilnehmerliste[1])
print(teilnehmerliste[-1])
print(teilnehmerliste[0:4])
print(teilnehmerliste[0:6:2]) #Jump by 2
print(teilnehmerliste[::3]) # jump by 3


###########################
# Access Sub list items
#~~~~~~~~~~~~~~~~~~
user_data = ["Thomas","Meier",["A", "B", "C"], True ]

print(user_data[1]) #Meier
print(user_data[2]) # ["A","B" "C"]

# Create the sub list
x = user_data[2] #["A","B","c"]
print(x)

# find the item:1 from the sublist
print(x[1]) #B

# Alternative Access sub list directly
print(user_data[[2][1]])

user_data = ["Thomas", "Meier" ,["A", "B","C",["AA", "BB"],["CC","DD"]]]


#AA
print(user_data[3][0])

#DD
print(user_data[3][2][1])
















