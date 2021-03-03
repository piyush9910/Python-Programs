# 6
"""list1 = [10, 20, 30, 40, 20, 50, 60, 40]
print("Original List : ",list1)
sett = set(list1)
list1 = list(sett)
print("List of unique numbers : ",sett)"""


# 7
"""list1=[]
n=int(input("Enter Range : "))
for i in range(n):
    list1.append(input("Enter string : "))
for i in list1:
    if i.endswith('a'):
        print(i, end= " ")"""

# 8
"""list1=[]
n=int(input("Enter Range : "))
for i in range(n):
    list1.append(input("Enter string : "))
for i in list1:
    if i.startswith('A'):
        print(i, end= " ")"""

# 9
"""X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(X)):
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)"""

# 10
"""X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]

for i in range(len(X)):
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)"""


#11
"""
list1=[10,50,10,2,3,4,8,9,6,5,48]
print("Original List : ",list1)
list1.sort()
list1.reverse()
print("Second Largest Element is : ",list1[1])
"""

#12
"""
lists = [10, 20, 30, 40, 50]
cu_list = []
length = len(lists)
cu_sum = [sum(lists[0:x:1]) for x in range(0, length + 1)]
print(cu_sum[1:])"""

#13
"""# Initialize list1ay     
list1 = [1, 2, 8, 3, 2, 2, 2, 5, 1]
# list1ay fr will store frequencies of element    
fr = [None] * len(list1)
visited = -1

for i in range(0, len(list1)):
    count = 1
    for j in range(i + 1, len(list1)):
        if (list1[i] == list1[j]):
            count = count + 1
            # To avoid counting same element again    
            fr[j] = visited

    if (fr[i] != visited):
        fr[i] = count;

    # Displays the frequency of each element present in list1ay    
print("---------------------")
print(" Element | Frequency")
print("---------------------")
for i in range(0, len(fr)):
    if (fr[i] != visited):
        print("    " + str(list1[i]) + "    |    " + str(fr[i]));
print("---------------------")"""


"""list = [1,2,3,4,5,4,1,5,2,6]
frequency = {}
for item in list:
   if (item in frequency):
      frequency[item] += 1
   else:
      frequency[item] = 1
for key, value in frequency.items():
   print("% d -> % d" % (key, value))
"""

# 14
"""list1=[]
n=int(input("Enter Range : "))
for i in range(n):
    list1.append(input("Enter Number : "))
for i in list1:
    if i.endswith(3) :
        print(i)"""

#15
"""s=int(input("enter starting range: "))
e=int(input("Enter ending range: "))
list1=[ i for i in range(s,e+1)]
print(list1)"""

# 16
"""list = [10, 1, 2, 20, 3, 20]
min = list.index (min(list))
max = list.index (max(list))
print("position of minimum element: ", min+1)
print("position of maximum element: ", max+1)

"""

# 17
"""a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=int(input("Enter element" +":"))
    a.append(element)
temp=a[0]
a[0]=a[n-1]
a[n-1]=temp
print("New list is:")
print(a)"""

# 18
"""
list1=[1,2,3,4,5,6]
n=len(list1)
temp=[]
j=n
for i in range(0,n):
    temp = list1[i]
    list1[i] = list1[j]
    list1[j] = temp

print(list1)"""

"""
#19
strings = ["Seeta", "Geeta", "Sham", "Ram"]
sorted_list = list(sorted(strings, key = len))
print(sorted_list)"""

# 20
"""list1=[1,2,3,4,5,6]
list2=[7,8,9,10]
print(list1+list2)"""

# 22
"""values = input("Input some comma seprated numbers : ")
list = values.split(",")
print('List : ',list)"""