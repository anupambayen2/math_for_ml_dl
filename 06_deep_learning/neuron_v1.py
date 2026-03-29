# Neuron Module

# Simple Neuron (No libraries)

def dot_product(v1, v2):
    result = 0
    for i in range(len(v1)):
        result += v1[i] * v2[i]
    return result


def neuron(inputs, weights, bias):
    return dot_product(inputs, weights) + bias


# Example data
inputs = [1, 2, 3]
weights = [0.5, 0.2, 0.1]
bias = 1

output = neuron(inputs, weights, bias)

print("Neuron Output:", output)