import math

while True:
    a = int(input("Enter a value: "))
    b = math.sqrt(a)

    if int(b) == b:
        print('good work')
        break
    else:
        print('Введи другое число!')
