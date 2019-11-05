# To display stars in the right angled triangular form
print("Part 1")
for i in range(1, 11):
    for j in range(1, i+1):
        print("*", end='')
    print()

#Equilateral Triangle
print("Part 2")
n=40
for i in range(1,11):
    print(' '*n, end='')
    print('* '*(i))
    n-=1

#Part 3
#Displaying numbers from 1 to 100 in 10 rows and 10 columns
print("Part 3")
for x in range(1, 11):
    for y in range(1, 11):
        print('{:8}'.format(x*y), end='')
    print()