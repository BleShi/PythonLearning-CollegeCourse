#编写程序，求小于100的所有合数。合数：指一个数除了它本身和1两个因数以外,还有别的因数。例如24,除了1和24还有2、3、4、6、8、12等因数。

nums=[]
for i in range (4,100):
  for j in range(2,i):
    if(i%j==0):
      nums.append(i)
      break

print(nums)