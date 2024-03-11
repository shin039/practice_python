import random
import pandas            as pd
import matplotlib.pyplot as plt
import seaborn           as sns
import japanize_matplotlib


# ゴルトンボード表示関数: 段数、玉数を指定する
def galton(steps, count):
  # 玉が落ちた位置を入れる空のリストを用意する
  ans = []

  # 指定された玉数だけくり返す
  for i in range(count):
    # 玉を落とす最初の位置を50にする
    val = 50

    # 指定された段数だけくり返す
    for j in range(steps):
      # 0か1のランダム、0なら-1、1なら+1
      if random.randint(0, 1) == 0:
        val = val - 1
      else :
        val = val + 1

    # 最終的に玉が落ちた位置をリストに追加する
    ans.append(val)

  # 落下した結果のリストをデータフレームにして
  df = pd.DataFrame(ans)
  # print(df.head())
  # print()

  # 0列目(落とした結果の列)をヒストグラムで表示する
  df[0].plot.hist()
  plt.title(str(steps) + "段: " + str(count) + "個")
  plt.ylabel("")
  plt.show()


galton( 1, 10000)
galton( 2, 10000)
galton( 6, 10000)
galton(10, 10000)


# importのunused警告を消すためだけの記述
japanize_matplotlib.japanize()
sns.set_theme()
