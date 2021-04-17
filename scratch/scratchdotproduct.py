# what is a dot product
# a = [1 ,2 ,3]
# b = [2, 3, 4]

# dot_product = a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
# print(dot_product)
import numpy as np
# inputs = [1, 2, 3, 2.5]
# weights = [0.2, 0.8, -0.5, 1.0]
# biases = 2

inputs = [1, 2, 3, 2.5]
weights = [
    [0.2, 0.8, -0.5, 1.0],
    [0.5, -0.91, 0.26, -0.5],
    [-0.26, -0.27, 0.17, 0.87]
    ]
biases = [2, 3, 0.5]

output = np.dot(weights, inputs) + biases
print(output)