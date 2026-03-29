import os

BASE_PATH = "/Users/anupambayen/projects/math_learning"

structure = {
    "00_foundation": [
        "variables.py",
        "loops.py",
        "functions.py"
    ],
    "01_linear_algebra": [
        "vectors.py",
        "matrices.py",
        "dot_product.py",
        "matrix_multiplication.py"
    ],
    "02_calculus": [
        "functions.py",
        "derivatives.py",
        "gradient.py"
    ],
    "03_probability": [
        "mean_variance.py",
        "distributions.py",
        "bayes.py"
    ],
    "04_numpy": [
        "basics.py",
        "vectorization.py"
    ],
    "05_ml_from_scratch": [
        "linear_regression.py",
        "gradient_descent.py",
        "loss_functions.py"
    ],
    "06_deep_learning": [
        "neuron.py",
        "activation.py",
        "backpropagation.py",
        "neural_network.py"
    ]
}


def create_structure():
    for folder, files in structure.items():
        folder_path = os.path.join(BASE_PATH, folder)
        os.makedirs(folder_path, exist_ok=True)

        for file in files:
            file_path = os.path.join(folder_path, file)
            if not os.path.exists(file_path):
                with open(file_path, "w") as f:
                    f.write(f"# {file.replace('.py', '').title()} Module\n\n")


if __name__ == "__main__":
    create_structure()
    print("Course structure created successfully!")