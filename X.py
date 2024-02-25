i=0
j=4
for row in range(5):
    for col in range(5):
        if((row== col)or (col==1 and row==3)  or (col==0 and row==4)):
            print("*", end="")
        elif(i==row and j==col):
             print("*", end="")
             i=i+1
             j=j-1
            
        else:
            print(end=" ")
    print()
