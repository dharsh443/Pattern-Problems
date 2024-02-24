for row in range(5):
    for col in range(4):
        if (col==0 or row==4 and (col>0 or col<4)):
            print("*", end="")
        else:
            print(end=" ")
    print()
