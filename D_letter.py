for i in range(6):
    for j in range(5):
        if ((j==0 or (i==0 or i==5)and(j<4)) or (j==4 and i!=0 and i!=5)):
            print("*",end="")
        else:
            print(end=" ")
    print()
