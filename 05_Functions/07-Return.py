
def addieren_1(x,y):
    result = x + y
    print("Result:",result)


    # with return
def addieren_2(x,y):
    result = x + y
    return result

# Multiple return
def addieren_3(x,y):
    result = x + y
    return result ,"Das Ergebnis beträgt" , True


# Caller
addieren_1(3,6)

# Single REturn 
total = addieren_2(50,60)
print("The result of two numbers is :", total)

# Multiple Returns
total, message, status = addieren_3(200,300)
print(total,message,status)