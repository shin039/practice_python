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
def relu(v):
    return np.maximum(v, 0)

# Test
print(relu(-5))
print(relu(3))
print(relu([0, 3, -1]))
