"""# Sum of digits of number
n=int(input("Enter a number:"))
tot=0
while(n>0):
    dig=n%10
    tot=tot+dig
    n=n//10
print("The total sum of digits is:",tot)


# Perfect Number
sum = 0
n=int(input("Enter a Number: "))
for x in range(1, n):
    if n % x == 0:
        sum += x
print(sum == n)

# Armstrong Number
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
"""

import math
a = 1
b = 10
c = -24
dis = b * b - 4 * a * c
sqrt_val = math.sqrt(abs(dis))
if dis > 0:
    print(" real and different roots ")
    print((-b + sqrt_val) / (2 * a))
    print((-b - sqrt_val) / (2 * a))

elif dis == 0:
    print(" real and same roots")
    print(-b / (2 * a))
else:
    print("Complex Roots")
    print(- b / (2 * a), " + i", sqrt_val)
    print(- b / (2 * a), " - i", sqrt_val)





