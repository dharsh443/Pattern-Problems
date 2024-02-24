for row in range(5):
    for col in range(6):
        if((col==0) or  ((row==0 or row==2 )and (col>0 and col<6))):
            print("*",end="")
        else:
            print(end=" ")
    print()
