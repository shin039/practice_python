# PyTorch Perceptron
import torch
import torch.nn as nn
import numpy    as np

# ------------------------------------------------------------------------------
# Initialise
# ------------------------------------------------------------------------------
# seed値を設定しておかないと、全結合層の定義時にバイアスと重みの初期値が毎回変わる
torch.manual_seed(1)

# ------------------------------------------------------------------------------
# Define Perceptron
# ------------------------------------------------------------------------------
D = 3 # input  Dimension
d = 2 # output Dimension

linear = nn.Linear(in_features=D, out_features=d, bias=True)

# ------------------------------------------------------------------------------
# Define Input Parameter
# ------------------------------------------------------------------------------
# torch.tensor 型の入力定義
#inputs = torch.randn(D)
inputs = torch.tensor(np.array([1, 2, 3]), dtype=torch.float32)

print("# Input")
print(inputs)
# print(inputs.dtype)

# ------------------------------------------------------------------------------
# Calc
# ------------------------------------------------------------------------------
outputs = linear(inputs)

print("\n# Output")
print(f"Size   => {outputs.size()}")
print(f"Output => {outputs}")

# ------------------------------------------------------------------------------
# Result
# ------------------------------------------------------------------------------
print(outputs)
print("\n# Linear Info")
print("weight: ", linear.weight)
print("bias  : ", linear.bias)
