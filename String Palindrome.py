my_str=input("Enter a String")
#my_str=my_str.casefold()
rev_str=reversed(my_str)
if list(my_str)==list(rev_str):
    print("It is Palindrome")
else:
    print("It is Not Palindrome")