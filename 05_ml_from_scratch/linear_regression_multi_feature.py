# Multi-variable Linear Regression

# Inputs (features)
X = [
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5]
]

# Output
y = [5, 8, 11, 14]  # roughly y = 2*x1 + 1*x2

# Initialize weights and bias
w = [0, 0]
b = 0
lr = 0.01

# Dot product
def dot(v1, v2):
    result = 0
    for i in range(len(v1)):
        result += v1[i] * v2[i]
    return result


# Training
for epoch in range(20):
    total_error = 0

    for i in range(len(X)):
        y_pred = dot(X[i], w) + b
        error = y_pred - y[i]

        # Update weights
        for j in range(len(w)):
            w[j] = w[j] - lr * error * X[i][j]

        # Update bias
        b = b - lr * error

        total_error += error**2

    print(f"Epoch {epoch}, w: {w}, b: {b:.4f}, Error: {total_error:.4f}")