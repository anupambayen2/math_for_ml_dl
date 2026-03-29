# Neural_Network Module

# Simple Neural Network Layer

import math

# Activation
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Dot product
def dot(v1, v2):
    result = 0
    for i in range(len(v1)):
        result += v1[i] * v2[i]
    return result

# Layer with 2 neurons
def layer(inputs, weights, biases):
    outputs = []

    for i in range(len(weights)):
        z = dot(inputs, weights[i]) + biases[i]
        a = sigmoid(z)
        outputs.append(a)

    return outputs


# Example
inputs = [1, 2]

weights = [
    [0.5, 0.2],   # neuron 1
    [0.3, 0.8]    # neuron 2
]

biases = [0.5, 0.1]

output = layer(inputs, weights, biases)

print("Layer Output:", output)