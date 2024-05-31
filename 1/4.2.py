while True:
    name = input("Enter your name: ")
    if name.isalpha() == False:
        print("You didn't enter a name")
        continue
    break
while True:
    surname = input("Enter your surname: ")
    if surname.isalpha() == False:
        print("You didn't enter a surname")
        continue
    break
while True:
    age = input("Enter your age: ")
    if age.isdigit() == False:
        print("You didn't enter a age")
        continue
    break
print("Your name: {}, surname: {}, age: {} years old.".format(name, surname, age))