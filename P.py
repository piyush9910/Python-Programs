def vowelwords():
    f=open('Text1.txt','r')
    N=f.read()
    M=N.split()
    for i in M:
        if i.startswith("A") or i.startswith("E") or i.startswith("I") or i.startswith("O") or i.startswith("U"):
            print("", end=" ")
        else:
            f2 = open("Text2.Txt", 'a')
            f2.write(i + ", ")

vowelwords()