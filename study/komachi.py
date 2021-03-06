# coding:UTF-8
# 小町算を行う。

# 足し算関数
def plus(x, y):
    return x + y

# 引き算関数
def minus(x, y):
    return x - y

# 2つの数字をジョインする。
def joinNumber(x, y):
    concat_num = str(x) + str(y)
    return int(concat_num)

# 演算式の表示
def komachi_disp(calc_keyno):
    express_str = ""
    for node in reversed(range(1, 10)):
        if node == 9:
            express_str += "9"
            continue
        calc_key = int(calc_keyno[node - 1])
        express_str += calcmark[calc_key] + str(node)
    return express_str

# N進数を求める。
def chgNRadix(target, radix):
    dv_no = int(target / radix)
    if dv_no < radix:
        return str(dv_no) + str(target % radix)
    return str(chgNRadix(dv_no, radix)) + str(target % radix)

# 関数リスト
funclist = [plus, minus, joinNumber]
calcmark = ["+", "-", ""]

#-------------------------------------------------
# Main
#-------------------------------------------------
func_num = len(funclist)

for base_no in range(func_num ** 8):
    calc_key_no     = ("00000000" + chgNRadix(base_no, func_num))[-8:]
    komachi_express = komachi_disp(calc_key_no)
    komachi_rslt    = eval(komachi_express)
    if komachi_rslt == 10:
        print(komachi_express, "=", komachi_rslt)
