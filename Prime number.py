n=int(input("Enter the Number- "))
if n>1:
    for i in range(2,n):
        if(n%i==0):
            print(n,"Not a Prime")
        break
    else:
        print(n,"is prime")
else:
    print(n,"Not a Prime")

