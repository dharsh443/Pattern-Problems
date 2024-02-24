for row in range(6):
    for col in range (4):
        if(col==0 or ((row==0 or row==5)and (col>0 or col<5))):
            print("*",end="")
        else:
            print(end=" ")
    print()
