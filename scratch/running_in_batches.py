import numpy as np

# keep in mind the dimension of the weights and biases remain the same 
# why because they define the hidden layer, the only thing that changed
# from single input run is that batch, so for each input run the weights
# have to be still the same.
# what we are trying to do is multiply each row
# in input to each row in weights (each row in weights is the
# same size as input as it is the input to one neuron)


inputs = [[1, 2, 3, 2.5],
        [1, 2, 3, 2.5],
        [1, 2, 3, 2.5]]
weights = [
    [0.2, 0.8, -0.5, 1.0],
    [0.5, -0.91, 0.26, -0.5],
    [-0.26, -0.27, 0.17, 0.87]
    ]
biases = [2, 3, 0.5]

output = np.dot(inputs, np.array(weights).T) + biases
print(output)