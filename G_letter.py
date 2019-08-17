for i in range(7):
    for j in range(6):
        if ((j==0 or (i==0 or i==6)and (j>0 and j<4))or (i==4 and j>1)or (j==3 and i!=2 and i!=3)):
            print("*",end="")
        else:
            print(end=" ")
    print()
