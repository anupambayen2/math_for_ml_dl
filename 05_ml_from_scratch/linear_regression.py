# Linear_Regression Module

# Linear Regression from Scratch

# Training data
x = [1, 2, 3, 4]
y = [2, 4, 6, 8]

# Initialize parameters
w = 0
b = 0
lr = 0.01

# Training
for epoch in range(20):
    total_error = 0 

    for i in range(len(x)):
        y_pred = w * x[i] + b
        error = y_pred - y[i]

        # update rules
        w = w - lr * error * x[i]
        b = b - lr * error

        total_error += error**2

    print(f"Epoch {epoch}, w: {w:.4f}, b: {b:.4f}, Error: {total_error:.4f}")