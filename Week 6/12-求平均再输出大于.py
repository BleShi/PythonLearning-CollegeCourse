# 设计一个函数，接收任意多个数,返回一系列值，其中第一个值为所有参数的平均值, 后面是所有大于平均值的数值。然后用不同的例子调用三次。

def average_above(*numbers):
    sum = 0
    above = []
    length = len(numbers)
    for index in range(0,length):
        sum+=numbers[index]

    average = sum/length

    for num in numbers:
        if num > average:
            above.append(num)

    return average, above

average1,above1 = average_above(12,34,56,78,102,14,26,64,81)

print(average1)
print(above1)