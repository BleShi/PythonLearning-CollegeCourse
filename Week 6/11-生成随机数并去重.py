# 随机生成20个(0-10)范围内的整数，剔除重复的数，并将剩下不重复的数进行从大到小的排序后，打印输出。

import random

a = [random.randint(0,10) for i in range(20)]

print(a)

unique_a = set(a) # 去重

print(unique_a)