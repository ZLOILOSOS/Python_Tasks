while True:
    x = input("Enter a three-digit number in which all numbers are different: ")
    if x == "exit":
        break
    elif x.isdigit():
        x1 = int(str(x)[0])
        x2 = int(str(x)[1])
        x3 = int(str(x)[2])
        if len(x) == 3 and x1 != x2 and x1 != x3 and x2 != x3:
            print(f"Number permutations {x}:")
            print(x1, x2, x3)
            print(x1, x3, x2)
            print(x2, x1, x3)
            print(x2, x3, x1)
            print(x3, x1, x2)
            print(x3, x2, x1)
        else:
            print("You entered a non-three-digit number or some of the numbers are the same")
    else:
        print("You did not enter a three-digit number")