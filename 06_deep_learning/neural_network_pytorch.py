# First PyTorch Model

import torch

# Data
X = torch.tensor([[1.0], [2.0], [3.0], [4.0]])
y = torch.tensor([[2.0], [4.0], [6.0], [8.0]])

# Model parameters
w = torch.tensor([0.0], requires_grad=True)
b = torch.tensor([0.0], requires_grad=True)

# Training
lr = 0.01

for epoch in range(20):

    # Forward pass
    y_pred = w * X + b

    # Loss (mean squared error)
    loss = ((y_pred - y) ** 2).mean()

    # Backward pass
    loss.backward()

    # Update weights
    with torch.no_grad():
        w -= lr * w.grad
        b -= lr * b.grad

    # Reset gradients
    w.grad.zero_()
    b.grad.zero_()

    print(f"Epoch {epoch}, w: {w.item():.4f}, b: {b.item():.4f}, Loss: {loss.item():.4f}")