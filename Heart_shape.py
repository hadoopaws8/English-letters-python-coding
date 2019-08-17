k=6
d=2
for i in range(6):
    for j in range(7):
        if (i==0 and j%3!=0)or(i==1 and j%3==0)or ((i==j+2)and i>1):
            print("*",end="")
        elif (i==d and j==k):
            print("*",end="")
            d+=1
            k-=1
        else:
            print(end=" ")
    print()
