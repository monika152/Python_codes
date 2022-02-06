
odd_number_list = ""
sum_odd_number = 0
count_odd_numbers = 0

lower_limit = int(input("Enter the lower limit:"))
upper_limit = int(input("Enter the upper limit:"))


for x in range(lower_limit, upper_limit) :
    if x%2 == 1 :
        odd_number_list += str(x)
        sum_odd_number += x
        count_odd_numbers += 1


        average_odd_numbers = sum_odd_number / count_odd_numbers

        print(f"All odd number between {lower_limit} and {upper_limit}:")
        print(f"All odd number: {odd_number_list}")
        print(f"sum of odd number: {sum_odd_number}")
        print(f"Average od odd number: {average_odd_numbers}")


