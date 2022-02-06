odd_list = []
odd = 0
odd_count = 0
sum_odd = 0
#list = [1,2,3,4,5,6,7,8,9,10,11,12]
for x in range(23):
    rem = x % 2
    if (rem != 0):
        odd_list.append(x)
           
        odd_count += 1
        sum_odd += x
       
print( "odd number are",odd_list)  
print("count of odd_number is", odd_count)
print("sum of odd no. is " , sum_odd)


       