odd_number_list =""
sum_odd_numbers = 0
count_odd_numbers = 0


lower_limit = int(input("enter the lower limit[only odd ]:"))
upper_limit = int(input("Enter the upper limit[only odd]:"))

#Correction
if lower_limit %2 == 0:
    lower_limit += 1



    for x in range(lower_limit, upper_limit+1, 2):

        odd_number_list += str(x) + ", "
        sum_odd_numbers += x
        count_odd_numbers += 1


average_odd_numbers = sum_odd_numbers / count_odd_numbers

print(f"All odd numbers between {lower_limit} and {upper_limit}:")
print(f"All odd numbers:{odd_number_list} and {upper_limit}")

