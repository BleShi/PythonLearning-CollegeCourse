# 求1！+2！+3！+4！+……+n! ，分别计算到n=10和20的和

sum10 = 0
sum20 = 0
calc = 1

n10 = 10 
n20 = 20 

for i in range (1,n10+1):
    calc = calc * i
    sum10 = sum10 +calc

for i in range (1,n20+1):
    calc = calc * i
    sum20 = sum20 +calc

print("n=10的和为：",sum10)
print("n=10和20的和为：", sum20)