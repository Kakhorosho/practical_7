n, k, r = map(int, input().split())

if n < r:
    count = 1
    c = k/100
    while r >= n:
        count += 1
        n = n*(1+c)
    print(count)
else:
    print(1)
