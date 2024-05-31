while True:
    x = input("Enter the number: ")
    if x == "exit":
        break
    elif x.isdigit():
        x = int(x)
        negative = 0
        positive = 0
        for x in range(-x, x + 2):
            print(x)
            if x < 0:
                negative += x
            else:
                positive += x
        print(f"The sum of negative numbers is {negative} and the sum of positive numbers is {positive}")
    else:
        print("You did not enter a number")