i=0
j=4

for row in range(5):
    for col in range(9):
        if((col==0 or col==8) or (col==5 and row==1) or (col==6 and row==2) or (col==7 and row==3)):
            print("*",end="")
        elif(row==i and col==j):
            print("*", end="")
            i=i+1
            j=j-1  
        else:
            print(end=" ")
    print()
