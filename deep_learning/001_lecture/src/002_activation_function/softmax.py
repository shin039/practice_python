
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
def softmax(v):
    x = np.array(v)
    x = x.T

    ### 問2-1 ###
    max_x = np.max(x, axis=0)

    ### 問2-2 ###
    e_x = np.exp(x - max_x)
    x = e_x / np.sum(e_x, axis=0)

    return x.T

# ------------------------------------------------------------------------------
# Test
# ------------------------------------------------------------------------------
# Test Data
x = np.array([
    [2.0, 1.0, 0.1],
    [1.0, 3.0, 0.2]
])

print(softmax(x))


# Torch
import torch
import torch.nn.functional as F

print(F.softmax(torch.tensor(x), 1))
