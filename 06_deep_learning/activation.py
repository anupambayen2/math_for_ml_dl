# Activation Module

# Activation Functions

import math

# -----------------------------------
# 1. Step Function
# -----------------------------------
def step_function(x):
    if x > 0:
        return 1
    else:
        return 0


# -----------------------------------
# 2. ReLU Function
# -----------------------------------
def relu(x):
    if x > 0:
        return x
    else:
        return 0


# -----------------------------------
# 3. Sigmoid Function
# -----------------------------------
def sigmoid(x):
    return 1 / (1 + math.exp(-x))


# -----------------------------------
# 4. Test values
# -----------------------------------
x_values = [-2, -1, 0, 1, 2]

print("Step Function:")
for x in x_values:
    print(x, "->", step_function(x))

print("\nReLU Function:")
for x in x_values:
    print(x, "->", relu(x))

print("\nSigmoid Function:")
for x in x_values:
    print(x, "->", sigmoid(x))