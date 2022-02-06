teilnehmerliste = ["Thomass" , "Ingo" ,"Sara", "Lena", "Jana", "Matthias"]

if "Thomas" in teilnehmerliste:
    print("TN is schon da")
else:
    print("TN ist nicht da")


if "bbb" not in teilnehmerliste:
    print("bbb does not exist")
else:
    print("bbb exists")


    ########################
    # Find  the index of a value:
    #~~~~~~~~~~~~~~~~~~~~~

    print(teilnehmerliste.index("Sara")) #2
    #print(teilnehmerliste.index("Banana")) #Error

    if "Banana" in teilnehmerliste: #False
        print(teilnehmerliste.index("Banana"))
    else:
        print("Banana ist nicht da")
