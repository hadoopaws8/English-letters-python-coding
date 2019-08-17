for i in range(4):
    for j in range(4-i):
        print("* ",end="")
    for j in range(i):
        print(4*" ",end="")
    for j in range(4-i):
        print("* ",end="")
    print()
for i in range(4):
    for j in range(i+1):
        print("* ",end="")
    for j in range(12-4*i):
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    print()
