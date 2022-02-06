
print("Willcommen bei Lidl")
print("~~~~~~~~~~~~~~~")

# ^Phase : Annahmen / Configuration / Einstellung
GLASS_PRICE = 0.08
PLASTIK_PRICE= 0.25
CURRENCY = "EURO"


# 1. Phase :User Inputs
count_glass =int(input("Anzahl von Glasflasher"))
count_plastik=int(input("Anzahl von Plastikfashe"))

# 2. Phase: calculation
result =count_glass*GLASS_PRICE + count_glass*PLASTIK_PRICE

#3. Print Results
print("Ihr Guthaben beträgt.",result,CURRENCY)