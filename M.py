for row in range (6):
    for col in range(5):
        if((col==0 or col==4) or row==1 and (col!=2) or row==2 and(col!=1 and col!=3)):
            print("*", end="")

        else:
            print(end=" ")
    print()
