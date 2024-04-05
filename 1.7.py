a = []
count = 0

for i in range(100, 1000):
    if i % 17 == 0:
        a.append(i)
        count += 1

print(a)
print(count)
