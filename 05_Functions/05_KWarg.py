
# **: Keyword Arguments --> dictionary of (key, value)
def greeting(**container):
    print(container)
    for key , val in container.items():
        print(f"Key:{key} Value:{val}")
        print()


    if "car" in container:
        print("Car key is available:", container.get("car"))
    else:
        print("Car key does not exists.")

# Caller
greeting(first_name = "Mohamed", last_name ="Ibrahim") # {'first_name': Mohamed,"last_name":Ibrahim}
greeting(id= 1, first_name = "Thomas",car = True) # {"id":1,"first_name":"Thomas", "Car":True}        

