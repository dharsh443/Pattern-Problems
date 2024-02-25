i=1
j=3
for row in range(5):
    for col in range(5):
        if (row==0 or row==4 and (col>0 or col<5)):
             print("*", end="")
        elif(i==row and col==j):
             print("*", end="")
             i=i+1
             j=j-1
        else:
            print(end=" ")
    print()
