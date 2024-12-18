import numpy as np

def type_check(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float, list, np.ndarray)):
                raise TypeError(f"引数はスカラーまたはNumPy配列が許容されます。")
        for key, value in kwargs.items():
            if not isinstance(value, (int, float, list, np.ndarray)):
                raise TypeError(f"引数はスカラーまたはNumPy配列が許容されます。")
        return func(*args, **kwargs)
    return wrapper


@type_check
def lrelu(x, alpha=0.01):
    """Leaky ReLU活性化関数を計算します。

    通常のReLU関数は負の値に対して0を返しますが、Leaky ReLUは負の値に対しても
    わずかな勾配を持つように改良されています。

    Args:
        x (float or np.ndarray): Leaky ReLU関数の入力となる実数またはNumPyの配列。
        alpha (float, optional): 負の値に対する勾配。デフォルトは0.01。

    Returns:
        float or np.ndarray: 入力の各要素に対するLeaky ReLU関数の結果。

    Raises:
        TypeError: 入力xやalphaが期待する型ではない場合。
        OverflowError: 計算中にオーバーフローが発生した場合。

    例:
        >>> lrelu(-0.5)
        -0.005
        >>> lrelu(0.5)
        0.5

    """
    try:
        with np.errstate(over='raise'):
            x =  np.maximum(x, x * alpha)
            return x
    except FloatingPointError as e:
        raise e


# ------------------------------------------------------------------------------
# Test
# ------------------------------------------------------------------------------
print(lrelu(-0.5))
print(lrelu(0.5))


x = np.array([1,-1,2])
d = np.array([-1,1,-2])
mask = x <= 0

out = x.copy()
## mask が Trueならoutを0に変換したい
out[mask] = 0
print(out)

dx = d.copy()
dx[mask] = d[mask] * 0
print(dx)
