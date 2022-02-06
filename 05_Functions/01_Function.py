# Prepare (define) the functions but not call them
def greeting1():
    print("Hallo WBS")
    print("Hallo DS")

def greeting2():
    for x in ["Thomas", "Ingo", "Sara", "Lena", "Jana","Matthias"]:
        print(f"Hallo{x}!")
        print(f"Welches BKG {x}?")
        print(f"Warum DS {x}?")
        print()


# Call the functions
greeting1()

print()

greeting2()