for row in range(7):
    for col in range(5):
        if(col==0 or col==1 and (row!=0 and row!=1 and row!=3 and row!=5 and row!=6) or col==2 and (row!=0 and row!=2 and
                                                                                                    row!=3 and row!=4 and row!=6)) or col==3 and(row!=1 and row!=2 and row!=3 and row!=4 and row!=5):
            print("*", end="")
        else:
            print(end=" ")
    print()
