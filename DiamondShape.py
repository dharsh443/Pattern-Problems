n=int(input("Enter the no of rows:"))
for i in range (0,n):
    for j in range(0,n-i-1):
        print(end=" ")
    for k in range(0,i+1):
        print("*",end=" ")
    print()
for l in range(n,0,-1):
    for m in range(0,n-l):
        print(end=" ")
    for o in range(0,l):
        print("*",end=" ")
    print()

