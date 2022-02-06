import re

# Specific Text format
"""
. : any charachter except (newline \n): placeholder
\. : A DOT
\d : digit 0-9
\D : not a digit
\w : Word a-z , A-Z, 0-9, _
\W : Not a word (dot, new line , TAB , Space)
\s : White Space
\S : not white Space
\b : Word Boundry
\B : Not a word Boundry

^ : Begin of a string
$ : end of string

{3} : except 3 places
{1,5} : min 1 and maximum 5
{,3} : max 3
{2,} ; min 2

[a-z] : range von a-z
[A-Z] : range von A-Z
[4-9] : range von 4-9
[a-zA-Z] : range von a-z & A-Z
[.-] : matches the charachter in brackets -> . & -

(a|b|c) : a or b or c

* : 0 or more
+ : one or more
? : 0 or one

"""

# Tokenizing

my_string = "I like python"

# 1. Option Native
mylist = my_string.split(" ")
print(mylist)

# 2. Option - with regex
mylist2 = re.split("\s+",my_string)
print(mylist2)

# Exracting some text --> example Emails
#################################
my_string = "For more information please email me at mohammed@abc.com , info@abc.com"

addresses = re.findall(r"[a-z]+[._]?[a-z]*@\w+\.[a-z]{2,4}",my_string)

for address in addresses:
    print(address)

# Replace some text --> replace emails
###########################################

my_string = "For more information please email me at xyz@abc.com"
my_new_string = re.sub(r"[a-z]+[._]?[a-z]*@\w+\.[a-z]{2,4}","info@abc.com",my_string)

print(my_string)
print(my_new_string)