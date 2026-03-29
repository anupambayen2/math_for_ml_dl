# Simple 2-Layer Neural Network

import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def dot(v1, v2):
    result = 0
    for i in range(len(v1)):
        result += v1[i] * v2[i]
    return result


def layer(inputs, weights, biases):
    outputs = []

    for i in range(len(weights)):
        z = dot(inputs, weights[i]) + biases[i]
        a = sigmoid(z)
        outputs.append(a)

    return outputs


# Input
inputs = [1, 2]

# Layer 1
weights1 = [
    [0.5, 0.2],
    [0.3, 0.8]
]
biases1 = [0.5, 0.1]

# Layer 2
weights2 = [
    [0.7, 0.6]
]
biases2 = [0.2]


# Forward pass
layer1_output = layer(inputs, weights1, biases1)
final_output = layer(layer1_output, weights2, biases2)

print("Final Output:", final_output)