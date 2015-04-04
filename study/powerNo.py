# coding:UTF-8
import math
import time
# 累乗数を求める。

base = 1
multiplicator = 2
num = 10

print('# 課題１ 通常ループ')
start = time.time()
for idx in range(num):
    base *= multiplicator
print(base)
print(time.time() - start)

print('# 課題２ 計算数を少なく。')
base = 1
multiplicator = 2
num = 11  # 1010 bit
loops = int(math.sqrt(num))
start = time.time()
while num > 0:
    # 仕組みがわかるよ。
    # print(num, num & 1, multiplicator, base)
    base *= multiplicator if num & 1 else 1
    multiplicator **= 2
    num >>= 1
print(base)
print(time.time() - start)
