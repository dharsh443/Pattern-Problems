for row in range(5):
    for col in range(5):
        if((col==2 and row>1) or (row == col and col<2)or (col==4 and row==0) or (col==3 and row==1)):
            print("*", end="")
        else:
            print(end=" ")
    print()
