for row in range(5):
    for col in range(5):
        if(row==0 and (col>0 or col<5) or col==2 or col==1 and (row!=1 and row!=2 and row!=3)):
            print("*", end="")
        else:
            print(end=" ")
    print()
