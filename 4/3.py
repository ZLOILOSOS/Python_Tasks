def write_text(text, file_name):
    with open(file_name, "a+") as file:
        file.write(text + "\n")


def print_even(file_name):
    global i
    with open(file_name, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        if i % 2 != 0:
            print(lines[i].strip())


write_text("11111", "3.txt")
write_text("22222", "3.txt")
write_text("33333", "3.txt")
write_text("44444", "3.txt")

print_even("3.txt")
