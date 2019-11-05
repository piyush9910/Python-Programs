str=input("Enter Elements Separated By Commas : ").split(',')
lst=[int(num) for num in str]
tup=tuple(str)

print('The Tuple is : ',tup)
ele=int(input("Enter Elements to Search : "))
try:
    pos=tup.index(ele)
    print('Element Position Number : ',pos+1)
exceptValueError:
        print('Element Not found.')