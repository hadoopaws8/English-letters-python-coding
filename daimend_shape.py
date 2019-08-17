for i in range(7):
    for j in range(7):
        if ((i-j==3)or(i+j==3 and j>0)or(j-i==3 and j>3)or((i==5 and j==4)or(i==4 and j==5))):
            print("*",end="")
        else:
            print(end=" ")
    print()
