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
def sigmoid(x):
    if isinstance(x, (list)):
        x = np.array(x)

    ### 問3 ###
    try:
        with np.errstate(over='raise'):
            return 1/ ( 1 + np.exp(-x))
    except FloatingPointError as e:
        raise e

# ------------------------------------------------------------------------------
# Test
# ------------------------------------------------------------------------------
print(sigmoid(0))
print(sigmoid([-1, 0, 1]))
print(sigmoid(99999999999999999999.0))

