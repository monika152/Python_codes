
values = []


for x in range(5):
    values.append(x*2)

print(values) # [0,2,4,6,8]



# Alternative
# Syntex: result = [ expression for items in items]


results = [x*2 for x in range(5)]
print(results) # [0,2,4,6,8]