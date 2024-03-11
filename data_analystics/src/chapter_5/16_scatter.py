# ------------------------------------------------------------------------------
# 分散と標準偏差
# ------------------------------------------------------------------------------
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Import
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import pandas            as pd
import matplotlib.pyplot as plt
import seaborn           as sns
import japanize_matplotlib

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# データ
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
data = {
  "ID": [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9],
  "A" : [59, 24, 62, 48, 58, 19, 32, 88, 47, 63],
  "B" : [49, 50, 49, 54, 45, 52, 56, 48, 45, 52],
}

df = pd.DataFrame(data)

# A
df.plot.scatter(x="ID", y="A", color="b", ylim=(0, 100))
plt.axhline(y=50, c="Magenta")
plt.title("Aのばらつき：大きい", fontsize=24)
plt.show()

# B
df.plot.scatter(x="ID", y="B", color="b", ylim=(0, 100))
plt.axhline(y=50, c="Magenta")
plt.title("Bのばらつき：小さい", fontsize=24)
plt.show()

# 平均値
meanA = df["A"].mean()
meanB = df["B"].mean()

# 標準偏差
stdA = df["A"].std()
stdB = df["B"].std()

print("データAは、約68%のデータが、", meanA - stdA, "～", meanA + stdA, "の範囲に収まっている。")
print("データBは、約68%のデータが、", meanB - stdB, "～", meanB + stdB, "の範囲に収まっている。")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# ヒストグラム
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
bins = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]

df["A"].plot.hist(bins=bins, color="c", ylim=(0, 6))
plt.axvline(x=meanA       , color="magenta")
plt.axvline(x=meanA - stdA, color="blue", linestyle="--")
plt.axvline(x=meanA + stdA, color="red" , linestyle="--")
plt.title("Aのばらつき: 大きい")
plt.show()

df["B"].plot.hist(bins=bins, color="c", ylim=(0, 6))
plt.axvline(x=meanB       , color="magenta")
plt.axvline(x=meanB - stdB, color="blue", linestyle="--")
plt.axvline(x=meanB + stdB, color="red" , linestyle="--")
plt.title("Bのばらつき: 小さい")
plt.show()

# importのunused警告を消すためだけの記述
japanize_matplotlib.japanize()
sns.set_theme()
