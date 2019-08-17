num=int(input("enter the number is a prime or not: "))
for i in range(2,num):
    if num%i==0:
        print(num," is not a prime")
        break
else:
    print(num," is a prime number")
