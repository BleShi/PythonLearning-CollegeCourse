# sum=1+1/2+1/3+1/4+⋯+1/n ，sum叫做调和级数，它是发散的。求当sum大于10时，n是多少；当sum大于20时，n又是多少。

sum1 = 0

for i in range(1,100000000):
    sum1 = sum1 + 1/i
    if sum1 > 10 :
        print(i)
        break

sum2 = 0

for j in range(1,10000000000000000):
    sum2 = sum2 + 1/j
    if sum2> 20 :
        print(j)
        break