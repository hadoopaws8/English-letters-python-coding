lower=int(input("enter lower element: "))
upper=int(input("enter upper element: "))
for i in range(lower,upper):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
