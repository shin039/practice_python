# NumPy Perceptron
import numpy  as np

x = np.array([1,2,3])

w = np.array([
  [1,1,1],
  [2,2,2]
])

b = np.array([5, 0])

print(type(x), x.shape, x)
print(type(w), w.shape, w)
print(type(b), b.shape, b)

ans1 = b + np.dot(w, x)
print(ans1)
