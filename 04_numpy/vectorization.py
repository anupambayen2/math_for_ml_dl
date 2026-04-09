# Vectorization Module

import numpy as np

# Data
X = np.array([[1, 2], [2, 3], [3, 4]])
w = np.array([0.5, 0.2])
b = 1

# Prediction (no loop)
y_pred = np.dot(X, w) + b

print("Predictions:", y_pred)
