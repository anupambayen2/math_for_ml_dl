# Functions Module

# Functions Module

# -----------------------------------
# 1. Function: Vector Addition
# -----------------------------------
def vector_add(v1, v2):
    result = []
    
    if len(v1) != len(v2):
        return "Error: Vectors must be same length"
    
    for i in range(len(v1)):
        result.append(v1[i] + v2[i])
    
    return result


# -----------------------------------
# 2. Function: Scalar Multiplication
# -----------------------------------
def scalar_multiply(vector, scalar):
    result = []
    
    for i in range(len(vector)):
        result.append(vector[i] * scalar)
    
    return result


# -----------------------------------
# 3. Function: Dot Product
# -----------------------------------
def dot_product(v1, v2):
    if len(v1) != len(v2):
        return "Error: Vectors must be same length"
    
    result = 0
    
    for i in range(len(v1)):
        result += v1[i] * v2[i]
    
    return result


# -----------------------------------
# 4. Test the functions
# -----------------------------------
v1 = [1, 2, 3]
v2 = [4, 5, 6]

print("Vector Add:", vector_add(v1, v2))
print("Scalar Multiply:", scalar_multiply(v1, 3))
print("Dot Product:", dot_product(v1, v2))
