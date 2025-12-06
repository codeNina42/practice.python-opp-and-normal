n=int(input("enter n:"))
for i in range(1,n+1):
    spaces=n-1
    stars=2*i-1
    print(" " * spaces + "*" * stars)
