# Vectors Module



# define vectors

v1 = [1,2,3]
v2 = [4,5,6]

print("v1",v1)
print("v2",v2)

# vector addition
v_add = []

for i in range(len(v1)):
    result = v1[i] + v2[i]
    v_add.append(result)


print("Vector addition", v_add)


# Scaler multiplication
scaler = 3
v_scaled = []

for i in range(len(v1)):
    result = v1[i] * scaler
    v_scaled.append(result)

print("Vector scaled", v_scaled) 

# Dot Product
dot_product = 0

for i in range(len(v1)):
    product = v1[i] * v2[i]

    dot_product +=product


print("Dot Product", dot_product)


# safety feature check
if len(v1) != len(v2):
    print("Error : vector must be same length")
else:
    print("Vector is in same length")