b = []
a = input()

for i in range(0, len(a) + 1):
    if i % 3 == 0:
        b.append(a[i-1])

print(b)
