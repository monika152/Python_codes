teilnehmerliste = [] # empty list

teilnehmerliste = ["Thomas" , "Ingo" ,"Sara", "Lena", "Jana", "Matthias"]
print(teilnehmerliste)

#List Methods:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#ADD
#~~~~~~~~~~~~~~~~~~~~~~~~
teilnehmerliste.append("Frank") # add the item to the end of the liste
print(teilnehmerliste)

teilnehmerliste.insert(2,"Sven") # add the item to a specific position
print(teilnehmerliste)


# Edit values:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
teilnehmerliste[0] = "Lane"
print(teilnehmerliste)


# Delete
#~~~~~~~~~~~~~~~
teilnehmerliste.pop() #delete the last item
print(teilnehmerliste)

teilnehmerliste.pop(1) # delete the specific  item
print(teilnehmerliste)

teilnehmerliste.remove("Jana") # delete the first match
print(teilnehmerliste)

#
