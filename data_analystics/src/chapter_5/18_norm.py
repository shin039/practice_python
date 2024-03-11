# ------------------------------------------------------------------------------
# Lesson 18. この値は普通なこと? 珍しいこと？
# ------------------------------------------------------------------------------
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Import
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
from scipy.stats import norm


mean  = 166.8 # 平均値
std   =   5.8 # 標準偏差

# 特定の値が上下の何%にあたるかどうかを調べる
# -> norm.cdf

value = 160.0 # 計測値

cdf = norm.cdf(x=value, loc=mean, scale=std)
print(value, "は、下から", cdf * 100, "%")
print(value, "は、上から", (1 - cdf) * 100, "%")
print()


# 全体の上下X%にあたる値は何かを調べる
# -> norm.ppf

per = 0.20 # 20%

ppf_under = norm.ppf(q=per      , loc=mean, scale=std)
ppf_upper = norm.ppf(q=(1 - per), loc=mean, scale=std)

print("下から", per * 100, "%の値は", ppf_under, "です。")
print("上から", per * 100, "%の値は", ppf_upper, "です。")
print()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# テストの平均点と標準偏差から点数の希少性を算出する
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# 数学
scoreM = 60
meanM  = 50
stdM   = 5

# 英語
scoreE = 80
meanE  = 70
stdE   = 8

cdf = norm.cdf(x=scoreM, loc=meanM, scale=stdM)
print("数学の", scoreM, "点は、上から", (1 - cdf) * 100, "%")

cdf = norm.cdf(x=scoreE, loc=meanE, scale=stdE)
print("英語の", scoreE, "点は、上から", (1 - cdf) * 100, "%")
