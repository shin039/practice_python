# ------------------------------------------------------------------------------
# Lesson 19. このデータは自然なばらつき？
# ------------------------------------------------------------------------------
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Import
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import pandas            as pd
import matplotlib.pyplot as plt
import seaborn           as sns
import numpy             as np
import japanize_matplotlib
from scipy.stats import norm

# 15個のデータで描画
df = pd.DataFrame({
  "A": np.random.randint( 0, 100, 15),
  "B": np.random.normal (50,  10, 15),
})

sns.distplot(df["A"], fit=norm, fit_kws={"color": "red"})
plt.title("かたよりのないランダムな値")
plt.show()

sns.distplot(df["B"], fit=norm, fit_kws={"color": "red"})
plt.title("正規分布になるようなランダムな値")
plt.show()

# 1500個のデータで描画
df = pd.DataFrame({
  "A": np.random.randint( 0, 100, 1500),
  "B": np.random.normal (50,  10, 1500),
})

sns.distplot(df["A"], fit=norm, fit_kws={"color": "red"})
plt.title("かたよりのないランダムな値")
plt.show()

sns.distplot(df["B"], fit=norm, fit_kws={"color": "red"})
plt.title("正規分布になるようなランダムな値")
plt.show()


# importのunused警告を消すためだけの記述
japanize_matplotlib.japanize()
sns.set_theme()
