for row in range(7):
    for col in range(5):
        if (col == 0 and row != 0) or (col in {1, 2, 4} and (row in {1, 2, 5, 6})) or (col == 3 and row != 0):
            print("*", end="")
        else:
            print(" ", end="")
    print()
