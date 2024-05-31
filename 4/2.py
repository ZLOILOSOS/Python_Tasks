def fibon(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b


n = 20
fibon = list(fibon(n))
print(fibon)
