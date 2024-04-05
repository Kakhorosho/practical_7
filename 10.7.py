k = 0
count = 0

while True:
    n = float(input())

    if 37.4 <= n <= 37.8:
        if k - n > 0:
            count += 1
        k = n
    else:
        if n != 0:
            print('wrong temperature')
            break
        print(count)
        break


