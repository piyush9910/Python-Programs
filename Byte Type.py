#Program to understand byte type array
#creates a list of byte numbers
elements=[10,20,30,40,50]
#creates the list into byte type array
x=bytes(elements)
#retrive elements from x using loop
for i in x:
    print(i)