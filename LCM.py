num1 = int(input("Enter a Number : "))
num2 = int(input("Enter a Number : "))
a = num1
b = num2
while(num2 != 0):   # When num2 is not equal to 0
# Swap num2 with num1 using temp
    temp = num2 #10
    num2 = num1 % num2   # Modulus of num1 and num2 # 0
    num1 = temp
gcd = num1
lcm = (a * b) // gcd   # LCM is found using HCF
print("HCF is : ",gcd)
print("LCM is : ",lcm)
exit()