# Complete Learning System

# Data
x = [1, 2, 3, 4]
y = [2, 4, 6, 8]

# Parameters
w = 0
b = 0
lr = 0.01

# Training
for epoch in range(20):

    total_error = 0

    for i in range(len(x)):

        # -------- Forward Pass --------
        y_pred = w * x[i] + b

        # -------- Error --------
        error = y_pred - y[i]

        # -------- Backpropagation --------
        w = w - lr * error * x[i]
        b = b - lr * error

        total_error += error**2

    print(f"Epoch {epoch}, w: {w:.4f}, b: {b:.4f}, Error: {total_error:.4f}")


# Final Prediction
print("\nFinal Prediction for x=5:", w*5 + b)