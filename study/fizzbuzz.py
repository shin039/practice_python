# coding:UTF-8

maxIdx = 999
fmtLen = len(str(maxIdx))

#
for idx in range(1, maxIdx+1):
    # idxをstringにして、rjustで空白フォーマットを調整。end=""で行末の改行を省略。
    print("%s: " % str(idx).rjust(fmtLen), end="")

    # 3の公倍数はFizz表記。
    if idx % 3 == 0:
        print("Fizz", end="")

    # 5の公倍数はBuzz表記。三項演算子を使用。
    print("Buzz" if idx % 5 == 0 else "", end="")

    # 行末の改行表示
    print()

