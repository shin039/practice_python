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
def tanh(x):
    """双曲線正接関数を計算します。

    双曲線正接関数は、双曲線正弦関数と双曲線余弦関数の比率として定義され、
    与えられた入力に対して-1と1の間の値を返します。ニューラルネットワークの
    活性化関数としてもよく使用されます。

    Args:
        x (float or np.ndarray): 双曲線正接関数の入力となる実数またはNumPyの配列。

    Returns:
        float or np.ndarray: 入力の各要素に対する双曲線正接関数の結果。

    Raises:
        TypeError: 入力xがfloatまたはnp.ndarray型ではない場合。
        OverflowError: 入力xの絶対値が大きすぎて、計算中にオーバーフローが発生した場合。

    例:
        >>> tanh(0)
        0.0
        >>> tanh(np.array([-1, 0, 1]))
        array([-0.76159416, 0.        , 0.76159416])

    """
    try:
        with np.errstate(over='raise'):
            ### 問4-1 ###
            sinh = (np.exp(x) - np.exp(-x))/2
            ### 問4-2 ###
            cosh = (np.exp(x) + np.exp(-x))/2  
            return sinh / cosh
    except FloatingPointError as e:
        raise e


# ------------------------------------------------------------------------------
# Test
# ------------------------------------------------------------------------------
print(tanh(0))
print(tanh(np.array([-1, 0, 1])))
