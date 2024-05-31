while True:
    list_counts = input("Введите числа через пробел: ")
    list_degree = []
    a = True
    counts = list_counts.split()
    for i in counts:
        if i.isdigit() == False:
            a = False
    if a == False:
        continue
    degree = input("Введите степень: ")
    if degree.isdigit() == False:
        continue
    for i in counts:
        list_degree.append(int(i) ** int(degree))
    print(list_degree)
    break
