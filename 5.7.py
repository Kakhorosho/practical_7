n = int(input())
a = int(n**(1/3))

while a != 0:
    b = a - 1
    c = b**3
    a = a - 1
    print(c, end=' ')