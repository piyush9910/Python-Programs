import random
"""def cls():
    print("\n")
def isEmpty(Qu):
    if Qu==[]:
        return True
    else:
        return False
def Enqueue(Qu,item):
    queue.append(item)
    if len(Qu)==1:
        front=rear=0
    else:
        rear=len(Qu)-1
def Dequeue(Qu):
    if isEmpty(Qu):
        return "Underflow"
    else:
        item=Qu.pop(0)
    if len(Qu)==0:
        front=rear=None
    return item
def peek(Qu):
    if isEmpty(Qu):
        return"Underflow"
    else:
        front=0
        return Qu[front]
def Display(Qu):
    if isEmpty(Qu):
        print("Queue Empty!")
    elif len(Qu)==1:
        print(Qu[0],"<==front,rear")
    else:
        front=0
        rear=len(Qu)-1
        print(Qu[front],"<-front")
        for a in range(1,rear):
            print(Qu[a])
        print(Qu[rear],"<-rear")
queue=[]
front=None
while True:
    cls()
    print("QUEUE OPERATIONS")
    print("1.Enqueue")
    print("2. Dequeue")
    print("3.Peek")
    print("4.Display Queue")
    print("5.Exit")
    ch=int(input("Enter your choice(1-5):"))
    if ch==1:
        item=int(input("enter item:"))
        Enqueue(queue,item)
        input("Press Enter to continue......")
    elif ch==2:
        item=Dequeue(queue)
        if item=="Underflow":
            print("Underflow! Queue is Empty!")
        else:
            print("Deque -ed item is",item)
        input("Press Enter to continue")
    elif ch==3:
        item=peek(queue)
        if item=="Underflow":
            print("Queue is empty!")
        else:
            print("Frontmost item is",item)
        input("Press Enter to continue..")
    elif ch==4:
        Display(queue)
        input("Press enter to continue....")
    elif ch==5:
        break
    else:
        print("invalid choice!")
        input("Press Enter to continue...... ")"""


"""import random
POINT=[30,50,20,40,45]
BEG=random.randint(1,3)
LAS=random.randint(2,4)
for C in range (BEG, LAS+1):
    print(POINT[C],"*",end="")


def Change(P ,Q=30):
    P=P+Q
    Q=P-Q
    print( P,"#",Q)
    return (P)
R=150
S=100
R=Change(R,S)
print(R,"#",S)
S=Change(S)"""


"""def count(s, c):
    res = 0
    for i in range(len(s)):
        if (s[i] == c):
            res = res + 1
    return res

str = input("Enter a String : ")
c = input("Enter String You want to find: ")
print(count(str, c))"""


AR=[20,30,40,50,60,70]
FROM=random.randint(1,3)
TO=random.randint(2,4)
for k in range(FROM,TO+1):
    print(AR[k], end="#")