#part 1
str='Hello'
for ch in str:
    print(ch)

#Part 2
str='Hello'
n=len(str)
for i in range(n):
    print(str[i])

#part 3 Odd Even
for i in range(0, 10, 2):
    print(i)


#Part 4

list =[10, 20, 30, 40, 50]
sum=0
for i in list:
    print(i)
    sum+=i
print("Sum = ",sum)