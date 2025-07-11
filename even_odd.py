
# create a code to find the even and odd numbers
def isEven_odd(n):
    if n%2==0:
        return "no is even"
    else:
        return "no is odd"
    # op= n%2==0 ? print("even"):print("odd")
    # print(op)
    

#write a code to find a prime no for the input
def isPrime(n):
    # if n<=1:
    #     return "no is not prime"
    # i=2

    # while n%i!=0:
    #     i += 1
    #     return "no is prime"

    # else:
    #     return "not prime"
    if n>1:
        c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2: #it only have 2 fators
        return "prime"
    else:
        return "not prime"

n=int(input("enter no: "))

isEven_odd(n)    
print(isPrime(n))