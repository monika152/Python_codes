
#Defination a string
course = "python"

print(course)

# Multi-line string
message ="""
Hallo Thomas,
wie geht es dir ?
lange nicht gesehen.
schöne Grüße
mattias
"""
print(message)

#string Function 
print(len(course ))




#slicing
course = "python programmierung"
print(course[0]) #p
print(course [20]) 
print(course[0:7])
print(course[-14:-1])
print(course[-1:-14])
print(course[:7])
print(course)

print() ,print()
print(course[0:])
print(course[:7])
print()
print(course[0:1])
print(),print(),print()
print(course[1:2])
# Escaping via \, \n :new line ,\t: TAB

print("Mohamed sagte \"guten Morgen \"heute")
print("mohamed sagte 'Guten Morgen ' heute ")
print()
# Alternativ
# two prints
print("monika")
print("singh")
print("monika\nSingh")
print("monika singh")
print("Monika\tsingh")
print("monika")


#string Formatting
first_name = "Monika"
last_name ="Singh"
#String concatenation
#full_name = first_name +"\t" +last_name
#full_name =first_name +""+last_name
full_name = first_name +last_name


#string methoden (Dot Function)
course=" pYthon progRMierunG "

print(course.upper())#PYTHON PROGRAMMIERUNG
print(course.lower())
print(course.title())
print(course.capitalize()) # ??

print(course.find("pro"))
print(course.replace("py" , "jy"))



#Method chain

print(course.strip().upper().lower())

user_name = input("Enter your name:").title()
print(user_name)

course =" pYThon proGraMmieRung "
course.upper().strip()
course.strip().upper()


print(course.strip().upper())

course = course.strip().upper() # strip remove extra spaces.
print(course)
len(course)