m1=[[1,2,3,0],
    [4,5,6,0],
    [7,8,9,0]
]

m2=[[1,2,3,0],
    [4,5,6,0],
    [7,8,9,0]
]

m3= [4*[0] for i in range(3)]

for i in range(3):
    for j in range(4):
      m3[i][j]=m1[i][j]+m2[i][j]
    print()



for i in range(3):
    for j in range(4):
        print('%d'%m3[i][j],end=" ")
    print()