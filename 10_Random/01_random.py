import random

# float
print(random.random()) # float number 0-1
print(random.uniform(2,20)) # float between 2-10 #TODO: what does uniform do here??

#integer
print(random.randint(2,20))# integer between 2-20 includes end point

print(random.randrange(2,20,2)) # integer between 2-20print(random.randit(2,20, step =2)
print(random.randrange(2,20,2))#integer between 2-20, step =2

# Selection 
#~~~~~~~~~~~~~~
teilnehmerliste = ["Thomas","Ingo","Sara","Lena","Jana","Matthias"]

#single choice
print(random.choice(teilnehmerliste))

# multiple choice --> with duplication k:count of required elements
print(random.choices(teilnehmerliste, k=3)) #["Ingo", "Jana","Jana"]
print(random.choices(teilnehmerliste, k=30)) # 30x items ["Matthias","Thomas",................"Thomas","Jana"]

# multiple choice -->without duplication
print(random.sample(teilnehmerliste, k= 4)) #["Mattias","Thomas", "Jana","Ingo"]

#Examples
print(random.choices(range(100),k = 4)) # [23,52,1,45,41,85,59,55,68,9]

# Shuffling
#~~~~~~~~~~~~~~~~~
numbers = [1,2,3,4,5,6,7,8]
print(numbers) #[1,2,3,4,5,6,7,8]

random.shuffle(numbers) # changes the original
print("Shuffled:", numbers) # Shuffled: [2,3,1,4,,6,5,7,8]