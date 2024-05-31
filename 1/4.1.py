ships = "Б1В1Г1 Е4Е5 В4В5В6В7 Д3 Д6 З2К2"
while True:
    x = input("Enter coordinate: ")
    if x == "exit":
        break
    elif len(x) == 2 and x[0].isalpha() and x[1].isdigit():
        if ships.find(x) >= 0 or ships.find(x.upper()) >= 0:
            print("Hit")
        else:
            print("Miss")
    else:
        print("You did not enter a coordinate")