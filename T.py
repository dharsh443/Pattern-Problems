for row in range(6):
    for col in range(6):
        if(row==0 and (col>0 or col<6) or col==2):
            print("*", end="")
        else:
            print(end=" ")
    print()
