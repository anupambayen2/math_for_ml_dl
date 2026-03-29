# Gradient_Descent Module

# Gradient Descent (Simple Intuition)

# Goal: Learn weight for y = wx

# Training data
x = [1, 2, 3, 4]
y = [2, 4, 6, 8]   # actual output (y = 2x)

# Initial weight
w = 0

# Learning rate
lr = 0.01

# Training loop
for epoch in range(10):
    total_error = 0

    for i in range(len(x)):
        y_pred = w * x[i]

        error = y_pred - y[i]

        # update rule
        w = w - lr * error * x[i]
            
        total_error += error**2

    print(f"Epoch {epoch}, Weight: {w:.4f}, Error: {total_error:.4f}")