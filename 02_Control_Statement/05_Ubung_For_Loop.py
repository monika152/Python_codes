all_numbers =""
positive_numbers = ""
negative_numbers = ""

sum_all = 0
sum_positive = 0
sum_negative = 0

# The user wish how many loops (input number) would like to have 
count_loops = int(input("Enter the numbers of loops:"))

for x in range(count_loops): # 10x Loops
    user_number = int(input("Enter number :"))
    all_numbers += str(user_number) + ","  ####??????
    sum_all += user_number


    if user_number >= 0: # positive number
        positive_numbers += str(user_number) +"."
        sum_positive += user_number

    else: # negative numbers
        negative_numbers += str(user_number) + " ,"
        sum_negative += user_number

        # Output
print("All numbers are: ", all_numbers)
print("POS Numbers are: ",sum_positive)
print("NEG Numbers are:",sum_negative)

print("Sum of all numbers: ", sum_all)
print("Sum of positive numbers: ", sum_positive)
print("Sum of negative numbers:",sum_negative)

#######################################################









































