# coding: UTF-8

# 素数計算
import math

# 事前準備
maxNo = 100  # 素数を計算する最大値
noList = [i for i in range(2, maxNo+1)]

calcNo = int(math.sqrt(maxNo))  # 素数を計算するための割り算につかう数字の最大値
divList = [i for i in range(2, calcNo+1)]

# 通常のやり方
# for divider in divList:
#     for target in noList:
#         noList.remove(target) if target % divider == 0 and target / divider != 1 else ""

# 1行でやってしまうやり方。
[noList.remove(target) for divider in divList for target in noList if (target % divider == 0 and target / divider != 1)]

# 素数表示
print(noList)
