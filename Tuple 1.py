# Sum and Average in Tuple
num=eval(input("Enter elements in (): "))
sum=0
n=len(num)
for i in range(n):
    sum+=num[i]
print('Sum of Numbers : ',sum)
print('Average of Numbers : ',sum/n)
