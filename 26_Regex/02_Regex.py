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



text_to_search = """
123.456.789.123
123-456-789-123
723-456-789-123
123A345B678C123

800.900.700.200
100.200.300.400
600.200.300.700
9999.200.300.800

6.200.300.400
77.200.300.800

Mohammed
Mr.Mohammed
Mr Mohammed

Meier
Mrs.Meier
Mr.Bayer

Mrs Meier

"""


#  Create Pattern
###############
pattern = re.compile(r"\d\d\d.\d\d\d.\d\d\d.\d\d\d")
pattern = re.compile(r"\d\d\d\..\d\d\d\..\d\d\d\.\d\d\d")

# Quantifiers
#~~~~~~~~~~~~~~~~~~~
pattern = re.compile(r"\d{3}\.\d{3}\.\d{3}\.\d{3}")
pattern = re.compile(r"\d{2,}\.\d{3}\.\d{3}\.\d{3}")
pattern = re.compile(r"\d{,2}\.\d{3}\.\d{3}\.\d{3}")

#Ranges
#~~~~~~~~~~~~~~~~
pattern = re.compile(r"[5-9]\d{2}[.-]\d{3}[.-]\d{3}[.-]\d{3}")

# Counts
#~~~~~~~~~~~~~~~
pattern = re.compile(r"\d+\.\d+\.\d+\.\d+")

# Selection
#~~~~~~~~~~~~~~~~~~~~
pattern =re.compile(r"Mr\.[A-Z][a-z]+") # Mr.Mohammed
pattern =re.compile(r"M(r|s|rs)\.?\s?[A-Z][a-z]+")

# Search the matches 
########################
matches = pattern.finditer(text_to_search)

# Loop over matches
################
for match in matches:
    print(match)