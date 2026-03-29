# Neuron with Activation

import math

def dot_product(v1, v2):
    result = 0
    for i in range(len(v1)):
        result += v1[i] * v2[i]
    return result


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def neuron(inputs, weights, bias):
    z = dot_product(inputs, weights) + bias
    return sigmoid(z)


# Example
inputs = [1, 2, 3]
weights = [0.5, 0.2, 0.1]
bias = 1

output = neuron(inputs, weights, bias)

print("Neuron Output (Probability):", output)