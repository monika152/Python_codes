class Participant:

    def __init__(self,name,city,id_nummer)-> None:
        self.name = name
        self.city = city
        self.__sensitive_data = id_nummer # Privatte attribute: using double under scores
        self.__banana = 0 # private attribute

    def greeting(self):
        self.__buchen()
        print(f"Name:{self.name}-ID:{self.__id_nummer}")

    def def__buchen(self): # private method
        print("Buchung ist durchgefürt !!")

thomas =Participant("Thomas Meier","Berlin","12345") 
Sara = Participant("Sara Meier","Berlin","456789")

print(thomas.name)
# print(thomas.id_number) # Error because the id_nummer is private

print(thomas.__dict__) #{'name': 'Thomas Meier', 'city': 'Berlin', '_Participents__sensitive_data': '12345', '_Participents__banana': 0}

#print(thomas._Participant__id_number) # Doch , ich kann privat memeber zugreifen

thomas.name = "Thomas Marc Meier"

print(thomas.__dict__)

thomas.Participant__id_number = "56789"
print(thomas.__dict__)

thomas.greeting()

thomas._Participant__buchen() # Doch , ich kann privat memeber zugreifen

