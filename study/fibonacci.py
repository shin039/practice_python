# coding:UTF-8
# フィボナッチ数列表示

# 表示回数
n = 10

# 再帰
print("再帰で実現")


def fbnc(first, second, num):
    num -= 1
    print(second, end=" ")
    if num <= 0:
        return
    fbnc(second, (first + second), num)


fbnc(0, 1, n)

# ループ
print()
print("ループで実現")
start = 1
nextval = 0
for i in range(n):
    start, nextval = nextval, nextval + start
    print(nextval, end=" ")
