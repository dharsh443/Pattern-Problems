for row in range(6):
    for col in range(5):
        if (col==0 or col==4 and (row!=3 and row!=4 and row!=5) or (row==0 or row==2) and (col>0 or col<5)):
            print("*",end="")
        else:
            print(end=" ")
    print()
