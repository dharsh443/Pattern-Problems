for row in range (6):
    for col in range(6):
        if(col==0 or col==5 or row==0 or row==5 and (col>0 or col<6)) :
           print("*", end="")
        else:
            print(end=" ")
    print()
