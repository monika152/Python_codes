def function1(): # outer function
    print("Hallo from outer function")

    def function2(): #inner function
        print("Hallo fron inner function")

    function2()

###main scope
function1()
print()

########################
def num1(x): # outer function
    print("X:",x)

    def num2(y): # inner function
        print("Y:",y)
        return x+y

    return num2 # returns the reference of num2

# main scope
myfunc1 = num1(5) # enthält die address von num2
print(myfunc1) # <function num1.<locals>.num2 at memory address

total = myfunc1(10) # calling the inner function num2
print("Total:",total)

#############################################
# use Factory

# 2^2,2^3,2^4
# 3^2,3^3.3^4

def power(num,power):
    return num ** power

# Alternative : factory of functions
def power_generator(num): # outer function

    def power_calc(power): # inner function
        return num**power

    return power_calc

# Generating the functions
power_two = power_generator(2)
power_three = power_generator(3)

# Calling the functions
print(power_two(3)) # 2^3
print(power_two(3)) #3^3


