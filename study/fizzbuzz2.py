# coding:UTF-8

maxIdx = 999
fmtLen = len(str(maxIdx))

# FizzBuzzを1行プログラミングしてみる。
#  if,forの三項演算子と、フォーマットで実現。
print("\n".join('{0}: {1}{2}'.format(str(idx).rjust(fmtLen), "Fizz" if idx % 3 == 0 else "", "Buzz" if idx % 5 == 0 else "") for idx in range(1, maxIdx + 1)))
