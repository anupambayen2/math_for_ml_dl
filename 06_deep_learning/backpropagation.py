# Backpropagation Module

# Simple Backpropagation (1 neuron)

import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


# Data
x = 1
y_true = 1

# Initialize weight
w = 0.5
lr = 0.1


# Training
for epoch in range(10):
    
    # Forward pass
    z = w * x
    y_pred = sigmoid(z)
    
    # Error
    error = y_true - y_pred
    
    # Backward pass (gradient)
    grad = error * sigmoid_derivative(y_pred) * x
    
    # Update
    w = w + lr * grad
    
    print(f"Epoch {epoch}, w: {w:.4f}, Error: {error:.4f}")