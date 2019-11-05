# Sorting of 3 Numbers without library and loop
x=int(input("Input First Number"))
y=int(input("Input First Number"))
z=int(input("Input First Number"))
a1=min(x,y,z)
a3=max(x,y,z)
a2=(x+y+z)-a1-a3
print("Number is Sorted ",a1,a2,a3)
