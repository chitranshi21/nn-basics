inputs = [1, 2, 3, 2.5]
weights = [
    [0.2, 0.8, -0.5, 1.0],
    [0.5, -0.91, 0.26, -0.5],
    [-0.26, -0.27, 0.17, 0.87]
    ]
biases = [2, 3, 0.5]

# for weight in zip(weights, biases):
#     print(weight)
# Zip takes all values and makes tuples out of it 

layer_outputs = []
for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_output = 0
    for n_input, n_weight in zip(inputs, neuron_weights):
        neuron_output += n_input * n_weight
    layer_outputs.append(neuron_output+neuron_bias)
print(layer_outputs)
