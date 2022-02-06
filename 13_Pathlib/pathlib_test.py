import os
from pathlib import Path
print(Path(__file__).parent)#c:\Users\Administrator\Desktop\python\13_Pathlib,shows absolute file path

os.chdir(Path(__file__).parent) # it change the cursor to our current file# it makes file path dynamic


with open("file1.txt") as file:
    print("Hallo ")

APP_FOLDER = Path(__file__).parent
print(APP_FOLDER)

mylist = list(APP_FOLDER.glob("*.txt"))
print(mylist)


for file in mylist:
    print(file)


file = Path(__file__).name
print(file) # shows the name of the file and its extension app.py

file = Path(__file__).name.split(".")[0] # display the name
print(file)



file = Path(__file__).name.split(".")[1] # display the extension of the file
print(file)

