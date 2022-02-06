numbers = [13,5,8,3,6,7,8,5,723,46]
print(numbers)


# 1. Variant : List Method: change the original list
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
numbers.sort() # asending (Aufsteigend)
print(numbers)

numbers.sort(reverse=True) # desending (Absteigend)
print(numbers)
print()

###########################################
# 2. Variant: It creates a new sorted list

numbers = [13,5,8,3,6,7,8,5,723,46]
sorted_list = sorted(numbers) # Aufsteigend
print(sorted_list)


sorted_list = sorted(numbers, reverse=True)
print(sorted_list)

