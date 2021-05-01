import math
layer_output = [4.8, 1.21, 2.385]

E = math.e

# The final value has to be a probability in a classification problem, the probability does not
# work well with negative values, so we need to way to preserve the information from negative values 
# while not dealing with negative values, enter E raised to power x

exp_values = [E**value for value in layer_output]
print(exp_values)

# Now we need to normailise this, normalise is basically the value devided by sum of all other values 
# so x/sum(of list of values) this gives us probability

sum_of_exp = sum(exp_values)
prob_values = [element/sum_of_exp for element in exp_values]
print(prob_values)
print("sum of total should be close to one " + str(sum(prob_values)))

# The above with numpy

import numpy as np

# we have a batch of output (for m training set)

layer_output = [[4.8, 1.21, 2.385],
                [4.8, 1.21, 2.385],
                [4.8, 1.21, 2.385]]
exp_values = np.exp(layer_output)
sum_of_exp = np.sum(exp_values, axis=1, keepdims=True)
prob_values = exp_values/sum_of_exp
print(prob_values)

