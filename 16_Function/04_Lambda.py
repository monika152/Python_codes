# classical

def double_1(x):
    return x*2

print(double_1(4))

# Alternative Lambda: anonymous function
# lambda argument(s): expression

double_2 = lambda x: x*2 # double_2 has the reference of the function
print(double_2(4)) 


##############################
# 2.Use Case --> By Sorting
product =[
    ("Product 1",15),
    ("Product 2",4),
    ("Product 3",50),
    ("Product 4",2)
]

product.sort(key=lambda item:item[1])
print(product)

#############################################
# 3.Use case --> by filter()

# classical way
my_list = [1,5,4,6,8,11,3,12]

def even_filter(my_list):
    my_even =[]
    for x in my_list:
        if x%2 == 0:
            my_even.append(x)

    return my_even

result = even_filter(my_list)
print(result)

# Alternative: with filter and lambda
result = list(filter(lambda x: (x%2 == 0), my_list))
print(result)

############################################
# 4. Use Case--> by map()
(my_list) = [1,5,4,6,8,11,3,12]

new_list = list(map(lambda x : x*2, my_list))

print(my_list)
print(new_list)