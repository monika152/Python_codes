# *variable_name == > The rest of the list -> sublist
numbers = [1,2,3,4,5,6]


#Unpack list in Variable 


first = numbers[0]
second =numbers[1]
third = numbers[2]

# Alternative using Unpacking
first, second ,third,*others = numbers #[1,2,3,4,5,6]
print(first, second,third,others) #1 2 3 [4,5,5]

# Unpacking
first,second, *others, last = numbers #[1,2,3,4]
print(first,second,others,last)