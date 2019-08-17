import time
k=0
d=4
for i in range(7):
    for j in range(5):
        if (j==0 or (i==j+2 and j>1)):
            print("*",end="")
            time.sleep(1)
        elif (i==k and j==d):
            print("*",end="")
            time.sleep(1)
            k+=1
            d-=1
        else:
            print(end=" ")
    print()
