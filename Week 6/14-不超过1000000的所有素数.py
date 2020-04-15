# 求不超过1000000的所有素数

for i in range(2, 1000001):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)