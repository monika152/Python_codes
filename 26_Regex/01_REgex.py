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



text_to_search = """abcdefghi
ABCDEFGHI
123456
abcdefghi


Mr.Mohammed
Mrs.Zimmermann
Mrs_Müller

google.com

my Name is Mohammed

jy PythonFy"""

# Create a pattern
######################

# Fixed Strings
pattern = re.compile("abc") # search for 'abc' in text
pattern = re.compile("google.com") # search for 'google.com' in text

pattern = re.compile(r"\d") # search for single digit
pattern = re.compile(r"\D") # search for  not single digit

pattern = re.compile(r"\w") # search for single word
pattern = re.compile(r"\W") # search for not single word

pattern = re.compile(r"^ab") # search for abc in the beginning of the string
pattern = re.compile(r"Fy$") # search for Fy at the end of the string


# search the matches
###########################
matches = pattern.finditer(text_to_search)

# Loop over matches
########################
for match in matches:
    print(match)