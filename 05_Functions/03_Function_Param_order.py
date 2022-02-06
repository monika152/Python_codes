def greeting(first_name, last_name, plz= ""):
    print(f"Hallo First Name: {first_name}, Last_Name:{last_name}, plz: {plz}")

    #Callers

    # Positional
    greeting("Thomas","Meier")
    greeting("Meier", "Thomas")

    # Keyword
    greeting(last_name = "Meier", first_name = "Ingo", plz = "25423")

    print(greeting("Monika","Singh"))